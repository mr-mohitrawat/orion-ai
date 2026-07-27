from orion.rag.embeddings import EmbeddingService
import numpy as np

embedding_service = EmbeddingService()

terraform = embedding_service.embeddings.embed_query(
    "Terraform provisions cloud infrastructure"
)

iac = embedding_service.embeddings.embed_query(
    "Infrastructure as Code tool"
)

python = embedding_service.embeddings.embed_query(
    "Python is a programming language"
)


def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


print("Terraform vs IaC")
print(cosine_similarity(terraform, iac))

print()

print("Terraform vs Python")
print(cosine_similarity(terraform, python))