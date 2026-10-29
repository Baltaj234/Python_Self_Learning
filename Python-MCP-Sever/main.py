"""MCP tools for looking up sample e-commerce data."""

from mcp.server.fastmcp import FastMCP

from transactional_db import CUSTOMERS_TABLE, ORDERS_TABLE, PRODUCTS_TABLE


mcp = FastMCP("ecommerce_tools")


@mcp.tool()
def get_customer_info(customer_id: str) -> dict[str, str]:
    """Get a customer's name and email address from their customer ID."""
    customer = CUSTOMERS_TABLE.get(customer_id)
    if customer is None:
        raise ValueError(f"No customer found with ID {customer_id!r}.")
    return {"customer_id": customer_id, **customer}


@mcp.tool()
def get_order_details(order_id: str) -> dict[str, str | list[str]]:
    """Get the customer, date, status, total, and items for an order ID."""
    order = ORDERS_TABLE.get(order_id)
    if order is None:
        raise ValueError(f"No order found with ID {order_id!r}.")
    return {"order_id": order_id, **order}


@mcp.tool()
def check_inventory(product_name: str) -> list[dict[str, str | int | float]]:
    """Find products whose names contain the query and return their stock."""
    query = product_name.strip().casefold()
    if not query:
        raise ValueError("Product name cannot be empty.")

    return [
        {"sku": sku, **product}
        for sku, product in PRODUCTS_TABLE.items()
        if query in str(product["name"]).casefold()
    ]


@mcp.tool()
def get_customer_ids_by_name(customer_name: str) -> list[str]:
    """Find customer IDs matching a full name, ignoring letter case."""
    query = customer_name.strip().casefold()
    if not query:
        raise ValueError("Customer name cannot be empty.")

    return [
        customer_id
        for customer_id, customer in CUSTOMERS_TABLE.items()
        if customer["name"].casefold() == query
    ]


@mcp.tool()
def get_orders_by_customer_id(
    customer_id: str,
) -> dict[str, dict[str, str | list[str]]]:
    """Get all orders placed by a customer ID."""
    if customer_id not in CUSTOMERS_TABLE:
        raise ValueError(f"No customer found with ID {customer_id!r}.")

    return {
        order_id: order
        for order_id, order in ORDERS_TABLE.items()
        if order["customer_id"] == customer_id
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
