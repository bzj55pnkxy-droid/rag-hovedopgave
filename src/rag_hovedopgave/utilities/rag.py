import os

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

# Use persistent Chroma instead of InMemoryVectorStore
PERSIST_DIR = "./chroma_db"

# Check if we already have embeddings saved
print(f"PERSIST_DIR exists: {os.path.exists(PERSIST_DIR)}")
if os.path.exists(PERSIST_DIR):
    print("Loading existing vector store from disk")
    vector_store = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=embeddings,
    )
else:
    print("Creating new vector store")
    # First time: load, split, and embed documents
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=0,
        add_start_index=True,
    )

    loader = DirectoryLoader(
        "./resources/java-curriculum-materials",
        glob="**/*.md",
        loader_cls=TextLoader,
    )

    docs = loader.load()
    for doc in docs:
        doc.metadata["semester"] = (
            "1st" if "1-semester" in doc.metadata["source"] else "2nd"
        )

    all_splits = text_splitter.split_documents(docs)
    for split in all_splits:
        semester = split.metadata["semester"]
        topic = (
            split.metadata["source"]
            .split("/")[-1]
            .replace("topic-", "")
            .replace("-", " ")
            .replace(".md", "")
        )
        split.page_content = (
            f"\nSemester: {semester}\nTopic: {topic}\n{split.page_content}"
        )

    vector_store = Chroma.from_documents(
        documents=all_splits,
        embedding=embeddings,
        persist_directory=PERSIST_DIR,
    )
    print("New vector store created.")
