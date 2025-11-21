from anthropic.types import ModelParam
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_chroma.vectorstores import Chroma
from langchain_cohere.embeddings import CohereEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import MarkdownHeaderTextSplitter

load_dotenv()

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
    # Extract 'difficulty' front-matter value and add it to the document metadata
    import re
    frontmatter_match = re.match(r"^---\n(.*?)\n---", doc.page_content, re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        difficulty_match = re.search(r'difficulty:\s*["\']?([A-Za-z0-9_-]+)["\']?', frontmatter)
        if difficulty_match:
            doc.metadata['difficulty'] = difficulty_match.group(1)

    print(doc.metadata)
    
model = ChatAnthropic(model="claude-haiku-4-5-20251001")

embeddings = CohereEmbeddings(model="embed-v4.0")

vector_store = Chroma(
    collection_name="Test",
    create_collection_if_not_exists=True,
    persist_directory=True,
    embedding_function=embeddings,
)

vector_store.add_documents(all_splits)

# To print the first entry in your vector store, you need to retrieve it using the appropriate method.
# Chroma does not support direct indexing like vector_store[0]. You can use .get or .as_retriever().get_relevant_documents.

# Example: Fetch the first document added (if you want to inspect the raw data)
first_doc = vector_store.get(ids=[vector_store._collection.get()['ids'][0]])['documents'][0]
print(first_doc)
