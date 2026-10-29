from __future__ import annotations

import json
import sys
from contextlib import AsyncExitStack, asynccontextmanager
from pathlib import Path
from typing import Any, AsyncIterator

import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import CallToolResult


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SERVER_PATH = PROJECT_ROOT / "main.py"
EXPECTED_TOOLS = {
    "get_customer_info",
    "get_order_details",
    "check_inventory",
    "get_customer_ids_by_name",
    "get_orders_by_customer_id",
}


@asynccontextmanager
async def async_client_session() -> AsyncIterator[ClientSession]:
    """Start the stdio server and return its connected MCP client session."""
    async with AsyncExitStack() as stack:
        server_params = StdioServerParameters(
            command=sys.executable,
            args=[str(SERVER_PATH)],
            cwd=str(PROJECT_ROOT),
        )
        read_stream, write_stream = await stack.enter_async_context(
            stdio_client(server_params)
        )
        session = await stack.enter_async_context(
            ClientSession(read_stream, write_stream)
        )
        await session.initialize()
        yield session


def parse_tool_result(result: CallToolResult) -> Any:
    """Decode a JSON result returned by a FastMCP tool."""
    if result.structuredContent is not None:
        return result.structuredContent.get("result", result.structuredContent)
    assert result.content
    return json.loads(result.content[0].text)


@pytest.mark.asyncio
async def test_server_exposes_expected_tools() -> None:
    async with async_client_session() as session:
        tools = await session.list_tools()

    assert {tool.name for tool in tools.tools} == EXPECTED_TOOLS


@pytest.mark.asyncio
async def test_customer_lookup_through_mcp_client() -> None:
    async with async_client_session() as session:
        result = await session.call_tool(
            "get_customer_info", {"customer_id": "CUST123"}
        )

    assert parse_tool_result(result) == {
        "customer_id": "CUST123",
        "name": "Alice Johnson",
        "email": "alice@example.com",
    }


@pytest.mark.asyncio
async def test_order_and_inventory_tools_through_mcp_client() -> None:
    async with async_client_session() as session:
        order_result = await session.call_tool(
            "get_orders_by_customer_id", {"customer_id": "CUST123"}
        )
        inventory_result = await session.call_tool(
            "check_inventory", {"product_name": "mouse"}
        )

    orders = parse_tool_result(order_result)
    inventory = parse_tool_result(inventory_result)
    assert set(orders) == {"ORD1001", "ORD1003"}
    assert inventory == [
        {"sku": "SKU100", "name": "Wireless Mouse", "stock": 42, "price": 24.99}
    ]


@pytest.mark.asyncio
async def test_unknown_customer_returns_tool_error() -> None:
    async with async_client_session() as session:
        result = await session.call_tool(
            "get_customer_info", {"customer_id": "UNKNOWN"}
        )

    assert result.isError
