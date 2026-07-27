from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    """
    Generates embeddings using a local Ollama model.
    """

    def __init__(
        self,
        model: str = "nomic-embed-text",
    ):
        self._embeddings = OllamaEmbeddings(
            model=model,
        )

    @property
    def embeddings(self):
        return self._embeddings