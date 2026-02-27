from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings,
)

results = vector_store.similarity_search("What is a database?", k=10)
print(f"\nFound {len(results)} results:\n")
for i, doc in enumerate(results, 1):
    print(f"    {doc.page_content}...\n")
