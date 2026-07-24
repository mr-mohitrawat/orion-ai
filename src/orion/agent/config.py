import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

MODEL = os.getenv("MODEL")

model = LiteLlm(
    model=MODEL,
)