
import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

OUTPUT_DIR = Path("data")
OUTPUT_DIR.mkdir(exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "Business_Sales_Data.csv"

products = {
    "Electronics": [
        ("Wireless Mouse", 650, 380),
        ("Keyboard", 1200, 720),
        ("Headphones", 1800, 1100),
        ("USB Cable", 250, 100),
        ("Bluetooth Speaker", 2200, 1450),
    ],
    "Home & Kitchen": [
        ("Water Bottle", 350, 180),
        ("Mixer Grinder", 2800, 2050),
        ("Storage Box", 500, 280),
        ("Cookware Set", 1900, 1300),
        ("Table Lamp", 850, 500),
    ],
    "Fashion": [
        ("T-Shirt", 499, 260),
        ("Jeans", 1299, 750),
        ("Backpack", 999, 550),
        ("Sports Shoes", 1999, 1250),
        ("Wallet", 399, 190),
    ],
    "Office Supplies": [
        ("Notebook Pack", 180, 90),
        ("Pen Set", 120, 55),
        ("Office Chair", 4500, 3300),
        ("Desk Organizer", 450, 240),
        ("Printer Paper", 320, 230),
    ],
}

regions = {
    "North": ["Delhi", "Lucknow", "Jaipur"],
    "South": ["Bengaluru", "Chennai", "Hyderabad"],
    "East": ["Kolkata", "Patna", "Bhubaneswar"],
    "West": ["Mumbai", "Pune", "Ahmedabad"],
}

channels = ["Online", "Retail Store", "Distributor"]
segments = ["Consumer", "Corporate", "Small Business"]
payment_methods = ["UPI", "Card", "Cash", "Net Banking"]

start_date = date(2025, 1, 1)
end_date = date(2026, 9, 30)
days_range = (end_date - start_date).days

rows = []

for order_id in range(1, 1501):
    order_date = start_date + timedelta(
        days=random.randint(0, days_range)
    )

    category = random.choice(list(products.keys()))
    product, unit_price, unit_cost = random.choice(
        products[category]
    )

    region = random.choice(list(regions.keys()))
    city = random.choice(regions[region])

    quantity = random.randint(1, 8)
    discount_pct = random.choice([0, 0, 0.05, 0.10, 0.15])

    gross_sales = unit_price * quantity
    discount_amount = round(gross_sales * discount_pct, 2)
    revenue = round(gross_sales - discount_amount, 2)
    cost = unit_cost * quantity
    profit = round(revenue - cost, 2)

    rows.append({
        "OrderID": f"ORD{order_id:05d}",
        "OrderDate": order_date.isoformat(),
        "Year": order_date.year,
        "Month": order_date.strftime("%b"),
        "MonthNumber": order_date.month,
        "Region": region,
        "City": city,
        "Category": category,
        "Product": product,
        "CustomerSegment": random.choice(segments),
        "SalesChannel": random.choice(channels),
        "PaymentMethod": random.choice(payment_methods),
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "DiscountPct": discount_pct,
        "Revenue": revenue,
        "Cost": cost,
        "Profit": profit,
    })

fields = list(rows[0].keys())

with OUTPUT_FILE.open("w", newline="", encoding="utf-8-sig") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print(f"Dataset created successfully: {OUTPUT_FILE}")
print(f"Total orders: {len(rows)}")
print(f"Total revenue: Rs {sum(r['Revenue'] for r in rows):,.2f}")
print(f"Total profit: Rs {sum(r['Profit'] for r in rows):,.2f}")
