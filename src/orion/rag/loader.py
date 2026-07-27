from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class DocumentLoader:
    """
    Loads documents from disk.
    """

    @staticmethod
    def load_pdf(path: str | Path) -> list[Document]:
        loader = PyPDFLoader(str(path))
        return loader.load()