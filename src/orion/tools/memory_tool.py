from google.adk.tools import Any, ToolContext
from google.adk.tools import FunctionTool

from ..memory.memory_service import memory_service


def remember_name(name: str, tool_context: ToolContext) -> str:
    """Remember the user's name."""

    user_id = tool_context.user_id

    memory_service.save(
        user_id=user_id,
        key="name",
        value=name,
    )

    return f"I'll remember your name is {name}."


def remember_language(language: str, tool_context: ToolContext) -> str:
    """Remember the user's preferred programming language."""

    user_id = tool_context.user_id

    memory_service.save(
        user_id=user_id,
        key="preferred_language",
        value=language,
    )

    return f"I'll remember your preferred language is {language}."


def get_name(tool_context: ToolContext) -> dict[str, Any]:
    """Get the user's name."""

    user_id = tool_context.user_id

    name = memory_service.get(user_id, "name")

    if name is None:
        return {
            "found": False,
            "name": None,
        }

    return {
        "found": True,
        "name": name,
    }



def get_preferred_language(tool_context: ToolContext) -> str:
    """Get the user's preferred programming language."""

    user_id = tool_context.user_id

    language = memory_service.get(
        user_id,
        "preferred_language",
    )

    if language:
        return language

    return "I don't know your preferred programming language yet."

memory_tools = [
    FunctionTool(remember_name),
    FunctionTool(remember_language),
    FunctionTool(get_name),
    FunctionTool(get_preferred_language),
]