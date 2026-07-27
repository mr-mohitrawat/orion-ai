from orion.rag.embeddings import EmbeddingService

embedding_service = EmbeddingService()

vector = embedding_service.embeddings.embed_query(
    "What is Terraform?"
)

print(type(vector))
print()

print(f"Vector Length: {len(vector)}")
print()

print(vector[:10])