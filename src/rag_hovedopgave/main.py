import os

from langchain_anthropic import ChatAnthropic
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)


model = ChatAnthropic(model="claude-sonnet-4-5-20250929")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def main():
    print("Hello from rag-hovedopgave!")


if __name__ == "__main__":
    main()
