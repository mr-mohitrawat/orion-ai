from pathlib import Path

from orion.rag.loader import DocumentLoader

docs = DocumentLoader.load_pdf(
    Path("src/orion/data/mohit.pdf")
)

print(f"Pages Loaded : {len(docs)}")

print()

print(docs[0].metadata)

print()

print(docs[0].page_content[:500])