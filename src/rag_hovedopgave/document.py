from typing import Any

import bs4
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.agents.middleware import (
    AgentMiddleware,
    AgentState,
    ModelRequest,
    dynamic_prompt,
    model_call_limit,
)
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_community.document_loaders import WebBaseLoader
from langchain_core import embeddings
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_cohere import CohereEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

model = ChatAnthropic(model="claude-")
embeddings = CohereEmbeddings(
    model="embed-v4.0",  # Multilingual, supports Danish + English cross-lingual retrieval
    input_type="search_document",  # Optimized for document indexing
)  # noqa: F811
vector_store = InMemoryVectorStore(embeddings)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)

bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    bs_kwargs={"parse_only": bs4_strainer},
)

docs = loader.load()

all_splits = text_splitter.split_documents(docs)

ids = vector_store.add_documents(documents=all_splits)

# @tool(response_format="content_and_artifact")
# def retrieve_context(query: str):
#     """Retrieve information to help answer a query."""
#     retrieved_docs = vector_store.similarity_search(query, k=2)
#     serialized = "\n\n".join(
#         (f"Source: {doc.metadata}\nContent: {doc.page_content}")
#         for doc in retrieved_docs
#     )
#     return serialized, retrieved_docs

# tools = [retrieve_context]

# prompt = (
#     "You have acess to a tool that retrieves context from a blog post. "
#     "Use the tool to help answer user queries"
# )
# agent = create_agent(model, tools, system_prompt=prompt)

# query = (
#     "What is the standard method for Task Decomposition?\n\n"
#     "Once you get the answer, look up common extensions of that method"
# )

# for event in agent.stream(
#     {"messages": [{"role": "user", "content": query}]},
#     stream_mode="values",
# ):
#     event["messages"][-1].pretty_print()

# @dynamic_prompt
# def prompt_with_context(request: ModelRequest) -> str:
#     """Inject context into state messages"""
#     last_query = request.state["messages"][-1].text
#     retrieved_docs = vector_store.similarity_search(last_query)

#     docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

#     system_message = (
#         "You're a helpful assistant. Use the following context in your response:"
#         f"\n\n{docs_content}"
#     )

#     print(f"\n\n **System message**: \n{system_message} \n**End system message**\n\n")

#     return system_message

# agent = create_agent(model, tools=[], middleware=[prompt_with_context])


class State(AgentState):
    context: list[Document]


class RetrieveDocumentsMiddleware(AgentMiddleware[State]):
    state_schema = State

    def before_model(self, state: AgentState) -> dict[str, Any] | None:
        last_message = state["messages"][-1]
        retrieved_docs = vector_store.similarity_search(last_message.text)

        docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)

        augmented_message_content = (
            f"{last_message.text}\n\nUse the following context to answer the query:\n{docs_content}"
        )
        return {
            "messages": [last_message.model_copy(update={"content": augmented_message_content})],
            "context": retrieved_docs,
        }


agent = create_agent(
    model,
    tools=[],
    middleware=[RetrieveDocumentsMiddleware()],
)

query = "What is task decomposition"
for step in agent.stream(
    {"messages": [{"role": "user", "content": query}]},
    stream_mode="values",
):
    step["messages"][-1].pretty_print()
