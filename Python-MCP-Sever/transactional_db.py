"""Small in-memory e-commerce tables for the MCP server example."""

CUSTOMERS_TABLE: dict[str, dict[str, str]] = {
    "CUST123": {
        "name": "Alice Johnson",
        "email": "alice@example.com",
    },
    "CUST456": {
        "name": "Bob Smith",
        "email": "bob@example.com",
    },
    "CUST789": {
        "name": "Carol Davis",
        "email": "carol@example.com",
    },
}

PRODUCTS_TABLE: dict[str, dict[str, str | int | float]] = {
    "SKU100": {
        "name": "Wireless Mouse",
        "stock": 42,
        "price": 24.99,
    },
    "SKU200": {
        "name": "Mechanical Keyboard",
        "stock": 18,
        "price": 79.99,
    },
    "SKU300": {
        "name": "USB-C Hub",
        "stock": 7,
        "price": 39.99,
    },
}

ORDERS_TABLE: dict[str, dict[str, str | list[str]]] = {
    "ORD1001": {
        "customer_id": "CUST123",
        "date": "2026-10-12",
        "status": "Shipped",
        "total": "$104.98",
        "items": ["Wireless Mouse", "Mechanical Keyboard"],
    },
    "ORD1002": {
        "customer_id": "CUST456",
        "date": "2026-10-20",
        "status": "Processing",
        "total": "$39.99",
        "items": ["USB-C Hub"],
    },
    "ORD1003": {
        "customer_id": "CUST123",
        "date": "2026-10-25",
        "status": "Delivered",
        "total": "$24.99",
        "items": ["Wireless Mouse"],
    },
}
