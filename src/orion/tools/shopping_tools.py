from google.adk.tools import ToolContext
from google.adk.tools import FunctionTool

def add_to_cart(product: str, tool_context: ToolContext) -> str:
    """Add a product to the shopping cart."""

    cart = tool_context.state.get("cart", [])

    cart.append(product)

    tool_context.state["cart"] = cart

    return f"{product} added to cart."


def show_cart(tool_context: ToolContext) -> str:
    """Show all products in the shopping cart."""

    cart = tool_context.state.get("cart", [])

    if not cart:
        return "Your cart is empty."

    return ", ".join(cart)


def clear_cart(tool_context: ToolContext) -> str:
    """Clear the shopping cart."""

    tool_context.state["cart"] = []

    return "Cart cleared."


shopping_tools = [
    FunctionTool(add_to_cart),
    FunctionTool(show_cart),
    FunctionTool(clear_cart),
]