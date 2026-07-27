from ..rag.retriever import Retriever
from google.adk.tools import FunctionTool

_retriever = Retriever()

def retrieve_documents(
    query: str,
    k: int = 4,
) -> str:
    """
    Search Orion's knowledge base and retrieve the most relevant information.

    Use this tool whenever the user's question requires information contained
    in indexed documents such as PDFs, manuals, documentation, research papers,
    or internal knowledge.

    Do not use this tool for:
    - greetings
    - arithmetic
    - general conversation
    - questions that do not require document lookup

    Args:
        query: Search query.
        k: Number of document chunks to retrieve.

    Returns:
        Retrieved document context.
    """


    documents = _retriever.retrieve(
        query=query,
        k=k,
    )

    if not documents:
        return "No relevant documents found."

    context = []

    for index, document in enumerate(documents, start=1):
        context.append(
            f"""
Document {index}

Source:
{document.metadata.get("source", "Unknown")}

Content:
{document.page_content}
"""
        )

    return "\n\n".join(context)


rag_tools = [
    FunctionTool(retrieve_documents)
]