from pathlib import Path

from langchain_chroma import Chroma

from ..rag.embeddings import EmbeddingService


class VectorStore:
    """
    Handles storage and retrieval of document embeddings.
    """

    def __init__(
        self,
        persist_directory: str | Path = "chroma_db",
        collection_name: str = "orion",
    ):
        self._embedding_service = EmbeddingService()

        self._vector_store = Chroma(
            collection_name=collection_name,
            persist_directory=str(persist_directory),
            embedding_function=self._embedding_service.embeddings,
        )

    @property
    def db(self) -> Chroma:
        return self._vector_store