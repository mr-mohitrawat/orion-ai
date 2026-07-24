from google.adk.agents import Agent
from .config import model
from .instructions import INSTRUCTION
from ..tools import tools

root_agent = Agent(
    name="orion",
    model=model,
    description="A simple AI assistant.",
    instruction=INSTRUCTION,
    tools=tools,
    )