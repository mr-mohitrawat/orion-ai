from datetime import datetime

from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmRequest, LlmResponse


def before_model_callback(
    callback_context: CallbackContext,
    llm_request: LlmRequest,
) -> LlmResponse | None:
    """
    Runs before every LLM call.
    """

    print("\n" + "=" * 60)
    print(" BEFORE MODEL CALLBACK")
    print("=" * 60)

    print(f"Time      : {datetime.now()}")
    print(f"Agent     : {callback_context.agent_name}")
    print(f"User ID   : {callback_context.user_id}")
    print(f"State     : {callback_context.state}")

    if llm_request.contents:
        last_message = llm_request.contents[-1]

        if last_message.parts:
            print(f"Message   : {last_message.parts[0].text}")

    print("=" * 60 + "\n")

    # Returning None tells ADK:
    # Continue with the normal LLM request.
    return None


def after_model_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse | None:
    print("=" * 60)
    print("AFTER MODEL CALLBACK")
    print("=" * 60)

    if llm_response.content:
        for part in llm_response.content.parts:
            if part.text:
                print(part.text)

    print("=" * 60)

    return None