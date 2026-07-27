from orion.rag.vector_store import VectorStore

db = VectorStore().db

print(db._collection.count())