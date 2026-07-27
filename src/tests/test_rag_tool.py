from orion.tools.rag_tools import retrieve_documents


def main():

    context = retrieve_documents(
        query="What is quantum computing?"
    )

    print(context)


if __name__ == "__main__":
    main()