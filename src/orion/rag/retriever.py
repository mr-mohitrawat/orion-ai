from langchain_core.documents import Document

from ..rag.vector_store import VectorStore


class Retriever:
    def __init__(self):
        self._vector_store = VectorStore().db

    def retrieve(
        self,
        query: str,
        k: int = 4,
    ) -> list[Document]:
        k = max(1, k)
        return self._vector_store.similarity_search(
            query=query,
            k=k,
        )

    def retrieve_with_score(
        self,
        query: str,
        k: int = 4,
    ) -> list[tuple[Document, float]]:
        return self._vector_store.similarity_search_with_score(
            query=query,
            k=k,
        )