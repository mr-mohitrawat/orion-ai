from pathlib import Path

from orion.rag.loader import DocumentLoader
from orion.rag.splitter import DocumentSplitter

documents = DocumentLoader.load_pdf(
    Path("src/orion/data/mohit.pdf")
)

print(f"Pages Loaded: {len(documents)}")

splitter = DocumentSplitter()

chunks = splitter.split(documents)

print(f"Chunks Created: {len(chunks)}")

print("\nFirst Chunk Metadata:")
print(chunks[0].metadata)

print("\nFirst Chunk:")
print(chunks[0].page_content)

print("\Second Chunk Metadata:")
print(chunks[1].metadata)

print("\nSecond Chunk:")
print(chunks[1].page_content)