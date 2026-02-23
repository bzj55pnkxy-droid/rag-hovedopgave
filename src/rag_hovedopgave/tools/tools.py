from langchain_core.tools import tool

from ..utilities.rag import vector_store


@tool
def search_curriculum(query: str, semester: str | None = None):
    """Search curriculum documents for information about Datamatiker courses and topics.

    Args:
        query: The search query to find relevant curriculum content.
        semester: Filter results by semester. Use "1st" for 1st semester or "2nd" for 2nd semester.
            Only include this when the student has indicated which semester they are on.
            Leave out to search across all semesters.
    """
    if semester:
        results = vector_store.similarity_search(
            query, k=4, filter={"semester": semester}
        )
    else:
        results = vector_store.similarity_search(query, k=4)

    return [doc.page_content for doc in results]
