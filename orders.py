"""Generate synthetic order data and save to `data/orders.csv`."""
from __future__ import annotations

import csv
import os
import random
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Iterable, List

from faker import Faker


fake = Faker()

ORDER_STATUSES = [
    "pending",
    "processing",
    "shipped",
    "delivered",
    "cancelled",
    "returned",
]


@dataclass
class Order:
    order_id: int
    customer_id: int
    order_date: str
    status: str


def generate_order(order_id: int, customer_range: range) -> Order:
    """Return a single synthetic order record."""
    customer_id = random.choice(customer_range)
    order_date = fake.date_time_between(start_date="-1y", end_date="now").isoformat()
    status = random.choice(ORDER_STATUSES)
    return Order(
        order_id=order_id,
        customer_id=customer_id,
        order_date=order_date,
        status=status,
    )


def generate_orders(count: int = 100, customer_count: int = 100) -> List[Order]:
    """Generate a list of synthetic orders."""
    customer_ids = range(1, customer_count + 1)
    return [generate_order(i + 1, customer_ids) for i in range(count)]


def write_orders(orders: Iterable[Order], filepath: str) -> None:
    """Write order data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = ["order_id", "customer_id", "order_date", "status"]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for order in orders:
            writer.writerow(asdict(order))


def main() -> None:
    orders = generate_orders(100, customer_count=100)
    write_orders(orders, os.path.join("data", "orders.csv"))
    print("Generated 100 orders at data/orders.csv")


if __name__ == "__main__":
    main()

