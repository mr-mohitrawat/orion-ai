from pathlib import Path

from ..rag.loader import DocumentLoader
from ..rag.splitter import DocumentSplitter
from ..rag.vector_store import VectorStore


class DocumentIngestor:
    def __init__(self):
        self._splitter = DocumentSplitter()
        self._vector_store = VectorStore()

    def ingest_pdf(self, pdf_path: str | Path) -> None:
        documents = DocumentLoader.load_pdf(pdf_path)

        chunks = self._splitter.split(documents)

        self._vector_store.db.add_documents(chunks)

        print(f"Ingested {len(chunks)} chunks.")