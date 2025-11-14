"""Generate synthetic product data and save to `data/products.csv`."""
from __future__ import annotations

import csv
import os
import random
from dataclasses import asdict, dataclass
from typing import Iterable, List

from faker import Faker


fake = Faker()

CATEGORIES = [
    "Electronics",
    "Home & Kitchen",
    "Fashion",
    "Beauty",
    "Sports",
    "Books",
    "Garden",
    "Toys",
    "Automotive",
    "Grocery",
]


@dataclass
class Product:
    product_id: int
    name: str
    category: str
    price: float
    stock: int


def generate_product(product_id: int) -> Product:
    """Return a single synthetic product record."""
    name = fake.catch_phrase()
    category = random.choice(CATEGORIES)
    price = round(random.uniform(5.0, 500.0), 2)
    stock = random.randint(0, 1000)
    return Product(
        product_id=product_id,
        name=name,
        category=category,
        price=price,
        stock=stock,
    )


def generate_products(count: int = 100) -> List[Product]:
    """Generate a list of synthetic products."""
    return [generate_product(i + 1) for i in range(count)]


def write_products(products: Iterable[Product], filepath: str) -> None:
    """Write product data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = ["product_id", "name", "category", "price", "stock"]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for product in products:
            writer.writerow(asdict(product))


def main() -> None:
    products = generate_products(100)
    write_products(products, os.path.join("data", "products.csv"))
    print("Generated 100 products at data/products.csv")


if __name__ == "__main__":
    main()

