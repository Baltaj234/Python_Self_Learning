# Python MCP Server

A small, beginner-friendly Model Context Protocol (MCP) server built with
Python's `mcp` package and `FastMCP`. It follows the hands-on flow in
[Real Python's Python MCP tutorial](https://realpython.com/python-mcp/):

1. Install the MCP SDK.
2. Create sample customer, order, and product tables.
3. Expose typed, documented functions as MCP tools.
4. Test the server through an MCP client over stdio.
5. Connect a compatible AI-agent client to the server.

The sample data is in memory, so changes disappear when the server restarts.
No API key or hosted language model is required to run the server or tests.

## Project files

- `main.py` creates the FastMCP server and registers the e-commerce tools.
- `transactional_db.py` contains the sample customer, order, and product data.
- `tests/test_server.py` starts the server over stdio and exercises it as an
  MCP client would.
- `requirements.txt` lists the server and test dependencies.

## Requirements

- Python 3.10 or later
- `pip`

## Install and test on Windows

Open a terminal in this project folder and create a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

If PowerShell prevents environment activation, run the environment's Python
directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest
```

The tests verify that an MCP client can discover the tools, call them, and
receive an error for an unknown customer.

## Run the MCP server

Start the server from this folder:

```powershell
python main.py
```

The server uses the stdio transport, so it waits for an MCP client and does not
display a regular interactive prompt. Stop it with `Ctrl+C` when running it
manually.

## Connect an AI agent

Add the server to an MCP-compatible client such as VS Code or Cursor. Configure
the client to launch the Python executable from this project's `.venv` and
pass the full path to `main.py` as its argument. For example, when adding this
project to the workspace root's `.vscode/mcp.json` on Windows:

```json
{
  "servers": {
    "python-ecommerce": {
      "type": "stdio",
      "command": "${workspaceFolder}\\Python-MCP-Sever\\.venv\\Scripts\\python.exe",
      "args": ["${workspaceFolder}\\Python-MCP-Sever\\main.py"]
    }
  }
}
```

If you opened this project folder itself as the workspace, remove the
`Python-MCP-Sever\\` segment from both paths. After restarting or refreshing
the MCP client, ask its agent questions such as “Which customer is
`CUST123`?” or “What is in stock for the wireless mouse?” Review and approve
tool calls in the client before they run.

## Available tools

- `get_customer_info(customer_id)` — return a customer's name and email.
- `get_order_details(order_id)` — return an order's details.
- `check_inventory(product_name)` — search product names and return stock.
- `get_customer_ids_by_name(customer_name)` — find a customer by full name.
- `get_orders_by_customer_id(customer_id)` — return all of a customer's orders.

Unknown customer and order IDs, and blank search terms, return tool errors
instead of silently producing misleading results.
