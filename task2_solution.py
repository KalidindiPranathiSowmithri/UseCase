import pandas as pd

customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")


customers_clean = customers.drop_duplicates()

print("Customers after removing duplicates:")
print(customers_clean)


invalid_orders = orders[
    ~orders["customer_id"].isin(customers_clean["customer_id"])
]

print("\nOrders with invalid customer IDs:")
print(invalid_orders)


valid_orders = orders[
    orders["customer_id"].isin(customers_clean["customer_id"])
]


merged_df = pd.merge(
    valid_orders,
    customers_clean,
    on="customer_id",
    how="inner"
)


merged_df = pd.merge(
    merged_df,
    products,
    on="product_id",
    how="inner"
)

merged_df["total_amount"] = (
    merged_df["quantity"] *
    merged_df["price"]
)


final_orders = merged_df[
    [
        "order_id",
        "customer_name",
        "city",
        "product_name",
        "quantity",
        "price",
        "status",
        "total_amount"
    ]
]


final_orders.to_csv(
    "final_orders.csv",
    index=False
)

print("\nFinal Orders:")
print(final_orders)
