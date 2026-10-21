
# Sales Data Analyzer
# A beginner-friendly introduction to data science.
# All sales records below are fictional mock data.

import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. CREATE MOCK DATA
# Each dictionary represents one customer order.
# --------------------------------------------------

sales_data = [
    {"date": "2026-01-05", "product": "Laptop Stand", "category": "Accessories", "units": 2, "unit_price": 35.00},
    {"date": "2026-01-12", "product": "Keyboard", "category": "Electronics", "units": 3, "unit_price": 60.00},
    {"date": "2026-01-19", "product": "Mouse", "category": "Electronics", "units": 5, "unit_price": 25.00},
    {"date": "2026-02-03", "product": "Laptop Stand", "category": "Accessories", "units": 4, "unit_price": 35.00},
    {"date": "2026-02-11", "product": "Headphones", "category": "Electronics", "units": 2, "unit_price": 90.00},
    {"date": "2026-02-20", "product": "Keyboard", "category": "Electronics", "units": 2, "unit_price": 60.00},
    {"date": "2026-03-02", "product": "Mouse", "category": "Electronics", "units": 8, "unit_price": 25.00},
    {"date": "2026-03-09", "product": "Laptop Stand", "category": "Accessories", "units": 3, "unit_price": 35.00},
    {"date": "2026-03-17", "product": "Headphones", "category": "Electronics", "units": 4, "unit_price": 90.00},
    {"date": "2026-03-25", "product": "Keyboard", "category": "Electronics", "units": 5, "unit_price": 60.00},
    {"date": "2026-04-04", "product": "Mouse", "category": "Electronics", "units": 6, "unit_price": 25.00},
    {"date": "2026-04-13", "product": "Laptop Stand", "category": "Accessories", "units": 5, "unit_price": 35.00},
    {"date": "2026-04-21", "product": "Headphones", "category": "Electronics", "units": 3, "unit_price": 90.00},
    {"date": "2026-05-06", "product": "Keyboard", "category": "Electronics", "units": 4, "unit_price": 60.00},
    {"date": "2026-05-14", "product": "Mouse", "category": "Electronics", "units": 10, "unit_price": 25.00},
    {"date": "2026-05-22", "product": "Laptop Stand", "category": "Accessories", "units": 2, "unit_price": 35.00},
    {"date": "2026-06-03", "product": "Headphones", "category": "Electronics", "units": 5, "unit_price": 90.00},
    {"date": "2026-06-12", "product": "Keyboard", "category": "Electronics", "units": 6, "unit_price": 60.00},
    {"date": "2026-06-19", "product": "Mouse", "category": "Electronics", "units": 7, "unit_price": 25.00},
    {"date": "2026-06-27", "product": "Laptop Stand", "category": "Accessories", "units": 6, "unit_price": 35.00},
]


# --------------------------------------------------
# 2. ORGANIZE THE DATA
# Turn the list of dictionaries into a DataFrame.
# A DataFrame is a table with rows and columns.
# --------------------------------------------------

df = pd.DataFrame(sales_data)

# Convert the date column into actual date values.
df["date"] = pd.to_datetime(df["date"])

# Calculate revenue for each order.
df["revenue"] = df["units"] * df["unit_price"]

print("\n===== SALES DATA =====")
print(df.to_string(index=False))


# --------------------------------------------------
# 3. CALCULATE BASIC STATISTICS
# --------------------------------------------------

total_revenue = df["revenue"].sum()
total_units = df["units"].sum()
total_orders = len(df)
average_order_value = df["revenue"].mean()

print("\n===== BUSINESS SUMMARY =====")
print(f"Total revenue: ${total_revenue:,.2f}")
print(f"Total units sold: {total_units}")
print(f"Number of orders: {total_orders}")
print(f"Average order value: ${average_order_value:,.2f}")
print(f"Highest order revenue: ${df['revenue'].max():,.2f}")
print(f"Lowest order revenue: ${df['revenue'].min():,.2f}")


# --------------------------------------------------
# 4. FIND THE BEST-SELLING PRODUCTS
# Group rows by product and add up their units.
# --------------------------------------------------

product_sales = df.groupby("product")["units"].sum()
product_sales = product_sales.sort_values(ascending=False)

print("\n===== UNITS SOLD BY PRODUCT =====")
print(product_sales.to_string())

best_product = product_sales.idxmax()

print(f"\nBest-selling product: {best_product}")


# --------------------------------------------------
# 5. COMPARE REVENUE BY PRODUCT CATEGORY
# --------------------------------------------------

category_revenue = df.groupby("category")["revenue"].sum()
category_revenue = category_revenue.sort_values(ascending=False)

print("\n===== REVENUE BY CATEGORY =====")

for category, revenue in category_revenue.items():
    print(f"{category}: ${revenue:,.2f}")


# --------------------------------------------------
# 6. ANALYZE MONTHLY REVENUE
# Group orders by month and calculate total revenue.
# --------------------------------------------------

df["month"] = df["date"].dt.to_period("M").astype(str)

monthly_revenue = df.groupby("month")["revenue"].sum()

print("\n===== MONTHLY REVENUE =====")

for month, revenue in monthly_revenue.items():
    print(f"{month}: ${revenue:,.2f}")

best_month = monthly_revenue.idxmax()

print(f"\nHighest-revenue month: {best_month}")


# --------------------------------------------------
# 7. CREATE CHARTS
# Visualize the results instead of only reading numbers.
# --------------------------------------------------

fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Bar chart: total units sold per product.
product_sales.plot(
    kind="bar",
    ax=axes[0],
    title="Units Sold by Product",
    xlabel="Product",
    ylabel="Units Sold",
)

axes[0].tick_params(axis="x", rotation=30)

# Line chart: revenue over time.
monthly_revenue.plot(
    kind="line",
    marker="o",
    ax=axes[1],
    title="Monthly Revenue",
    xlabel="Month",
    ylabel="Revenue ($)",
)

axes[1].tick_params(axis="x", rotation=30)

plt.tight_layout()
plt.show()
