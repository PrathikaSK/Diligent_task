"""Generate synthetic payment data and save to `data/payments.csv`."""
from __future__ import annotations

import csv
import os
import random
from dataclasses import asdict, dataclass
from typing import Iterable, List

from faker import Faker


fake = Faker()

PAYMENT_METHODS = [
    "credit_card",
    "debit_card",
    "paypal",
    "bank_transfer",
    "gift_card",
    "cash_on_delivery",
]


@dataclass
class Payment:
    payment_id: int
    order_id: int
    amount: float
    payment_method: str
    payment_date: str


def generate_payment(payment_id: int, order_range: range) -> Payment:
    """Return a single synthetic payment record."""
    order_id = random.choice(order_range)
    amount = round(random.uniform(10.0, 1000.0), 2)
    payment_method = random.choice(PAYMENT_METHODS)
    payment_date = fake.date_time_between(start_date="-1y", end_date="now").isoformat()
    return Payment(
        payment_id=payment_id,
        order_id=order_id,
        amount=amount,
        payment_method=payment_method,
        payment_date=payment_date,
    )


def generate_payments(count: int = 100, order_count: int = 100) -> List[Payment]:
    """Generate a list of synthetic payments."""
    order_ids = range(1, order_count + 1)
    return [generate_payment(i + 1, order_ids) for i in range(count)]


def write_payments(payments: Iterable[Payment], filepath: str) -> None:
    """Write payment data to a CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    fieldnames = ["payment_id", "order_id", "amount", "payment_method", "payment_date"]

    with open(filepath, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for payment in payments:
            writer.writerow(asdict(payment))


def main() -> None:
    payments = generate_payments(100, order_count=100)
    write_payments(payments, os.path.join("data", "payments.csv"))
    print("Generated 100 payments at data/payments.csv")


if __name__ == "__main__":
    main()

