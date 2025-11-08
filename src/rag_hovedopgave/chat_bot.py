from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
from langchain_chroma.vectorstores import Chroma
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_core import embeddings
from langchain_text_splitters.markdown import (
    MarkdownHeaderTextSplitter,
)
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

# Use TextLoader to preserve raw markdown formatting including headers
loader = DirectoryLoader(
    "./src/rag_hovedopgave/resources/example-data",
    glob="**/*.md",
    loader_cls=TextLoader,
)

docs = loader.load()

headers_to_split = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]

markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split,
    strip_headers=False,
)

all_splits = []

for doc in docs:
    all_splits.extend(markdown_splitter.split_text(doc.page_content))

# print(f"Total documents loaded: {len(docs)}")
# print(f"Total chunks after splitting: {len(all_splits)}")
# print(f"\nFirst chunk:\n{all_splits[0].metadata}")

# model: ModelParam = "claude-haiku-4-5-20251001"

model = ChatAnthropic(model="claude-haiku-4-5-20251001")

embeddings = CohereEmbeddings(model="embed-v4.0")

vector_store = Chroma(
    collection_name="Test",
    create_collection_if_not_exists=True,
    persist_directory=True,
    embedding_function=embeddings,
)

vector_store.add_documents(all_splits)


@tool(response_format="content_and_artifact")
def retrieve_context(query: str):
    """Retrieve information to help answer a query"""
    retrieved_docs = vector_store.similarity_search(query, k=3)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}") for doc in retrieved_docs
    )
    return serialized, retrieved_docs


tools = [retrieve_context]

prompt = (
    "You have access to a tool that retrieves context from a blog post. "
    "Use the tool to help answer user queries."
)

while True:

    query = input("Hi, what can I help you with?: ")

    agent = create_agent(model, tools, system_prompt=prompt, checkpointer=InMemorySaver())

    for token, metadata in agent.stream(
        {"messages": [{"role": "user", "content": query}]},
        stream_mode="messages",
    ):
        print(token.content_blocks)

