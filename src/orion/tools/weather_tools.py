from google.adk.tools import FunctionTool


def get_weather(city: str) -> str:
    """
    Get the current weather for a city.

    This is currently a mock implementation.
    """
    return f"The weather in {city} is sunny with a temperature of 28°C."


weather_tools = [
    FunctionTool(get_weather),
]