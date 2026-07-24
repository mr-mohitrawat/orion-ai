from datetime import datetime

from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import ToolContext, BaseTool


def before_tool_callback(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext,
):
    print("\n" + "=" * 60)
    print("BEFORE TOOL CALLBACK")
    print("=" * 60)

    print(f"Time      : {datetime.now()}")
    print(f"Agent     : {tool_context.agent_name}")
    print(f"User ID   : {tool_context.user_id}")
    print(f"Tool Name : {tool.name}")
    print(f"Arguments : {args}")

    print("=" * 60 + "\n")

    return None
def after_tool_callback(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext,
    tool_response,
):
    print("\n" + "=" * 60)
    print("AFTER TOOL CALLBACK")
    print("=" * 60)

    print(f"Tool Name : {tool.name}")
    print(f"Arguments : {args}")
    print(f"Response  : {tool_response}")

    print("=" * 60 + "\n")

    return None