"""Generate synthetic customer data and save to `data/customers.csv`."""
from __future__ import annotations

import csv
import os
from dataclasses import asdict, dataclass
from datetime import datetime
from typing import Iterable, List

from faker import Faker


fake = Faker()


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone: str
    address: str
    created_at: str


def generate_customer(customer_id: int) -> Customer:
    """Return a single synthetic customer record."""
    return Customer(
        customer_id=customer_id,
        name=fake.name(),
        email=fake.unique.email(),
        phone=fake.phone_number(),
        address=fake.address().replace("\n", ", "),
        created_at=fake.date_time_between(start_date="-2y", end_date="now").isoformat(),
    )


def generate_customers(count: int = 100) -> List[Customer]:
    """Generate a list of synthetic customers."""
    return [generate_customer(i + 1) for i in range(count)]


def write_customers(customers: Iterable[Customer], filepath: str) -> None:
    """Write customer data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = ["customer_id", "name", "email", "phone", "address", "created_at"]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for customer in customers:
            writer.writerow(asdict(customer))


def main() -> None:
    customers = generate_customers(100)
    write_customers(customers, os.path.join("data", "customers.csv"))
    print("Generated 100 customers at data/customers.csv")


if __name__ == "__main__":
    main()

