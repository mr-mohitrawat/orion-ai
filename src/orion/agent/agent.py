from google.adk.agents import Agent
from .config import model
from .instructions import INSTRUCTION
from ..tools import tools
from ..callbacks.model_callbacks import before_model_callback, after_model_callback
from ..callbacks.tool_callbacks import before_tool_callback,after_tool_callback

root_agent = Agent(
    name="orion",
    model=model,
    description="A simple AI assistant.",
    instruction=INSTRUCTION,
    tools=tools,

    # Model callbacks
    before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,

    # Tool callbacks
    before_tool_callback=before_tool_callback,
    after_tool_callback=after_tool_callback,
    )