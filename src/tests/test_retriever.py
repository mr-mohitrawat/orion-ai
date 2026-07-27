from orion.rag.retriever import Retriever


def main():
    retriever = Retriever()

    query = "What is quantum computing?"

    results = retriever.retrieve_with_score(
        query=query,
        k=4,
    )

    print(f"\nQuery: {query}")
    print(f"Retrieved {len(results)} document(s).\n")

    for index, (document, score) in enumerate(results, start=1):
        print("=" * 100)
        print(f"Document {index}")
        print("=" * 100)
        print(f"Similarity Score: {score:.4f}\n")

        if document.metadata:
            print("Metadata:")
            for key, value in document.metadata.items():
                print(f"  {key}: {value}")
            print()

        print("Content:")
        print(document.page_content)
        print()


if __name__ == "__main__":
    main()