"""Generate synthetic order item data and save to `data/order_items.csv`."""
from __future__ import annotations

import csv
import os
import random
from dataclasses import asdict, dataclass
from typing import Iterable, List, Tuple

from faker import Faker


fake = Faker()


@dataclass
class OrderItem:
    order_item_id: int
    order_id: int
    product_id: int
    quantity: int
    price: float


def generate_order_item(order_item_id: int, order_range: range, product_range: range) -> OrderItem:
    """Return a single synthetic order item record."""
    order_id = random.choice(order_range)
    product_id = random.choice(product_range)
    quantity = random.randint(1, 5)
    price = round(random.uniform(5.0, 500.0), 2)
    return OrderItem(
        order_item_id=order_item_id,
        order_id=order_id,
        product_id=product_id,
        quantity=quantity,
        price=price,
    )


def generate_order_items(
    count: int = 100,
    order_count: int = 100,
    product_count: int = 100,
) -> List[OrderItem]:
    """Generate a list of synthetic order items."""
    order_ids = range(1, order_count + 1)
    product_ids = range(1, product_count + 1)
    return [generate_order_item(i + 1, order_ids, product_ids) for i in range(count)]


def write_order_items(order_items: Iterable[OrderItem], filepath: str) -> None:
    """Write order item data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = ["order_item_id", "order_id", "product_id", "quantity", "price"]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for order_item in order_items:
            writer.writerow(asdict(order_item))


def main() -> None:
    order_items = generate_order_items(100, order_count=100, product_count=100)
    write_order_items(order_items, os.path.join("data", "order_items.csv"))
    print("Generated 100 order items at data/order_items.csv")


if __name__ == "__main__":
    main()

