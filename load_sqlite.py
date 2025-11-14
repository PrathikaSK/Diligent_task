"""Load generated CSV data into an SQLite database."""
from __future__ import annotations

import os
import sqlite3
from pathlib import Path

import pandas as pd


DATA_DIR = Path("data")
DB_PATH = Path("ecom.db")

TABLE_FILES = {
    "customers": DATA_DIR / "customers.csv",
    "products": DATA_DIR / "products.csv",
    "orders": DATA_DIR / "orders.csv",
    "order_items": DATA_DIR / "order_items.csv",
    "payments": DATA_DIR / "payments.csv",
}


def ensure_files_exist() -> None:
    """Validate that all required CSV files are present."""
    missing = [str(path) for path in TABLE_FILES.values() if not path.exists()]
    if missing:
        raise FileNotFoundError(f"Missing CSV files: {', '.join(missing)}")


def create_connection(db_path: Path) -> sqlite3.Connection:
    """Create an SQLite connection."""
    return sqlite3.connect(db_path)


def load_tables(conn: sqlite3.Connection) -> None:
    """Load CSV files into SQLite tables using pandas."""
    for table, csv_path in TABLE_FILES.items():
        df = pd.read_csv(csv_path)
        df.to_sql(table, conn, if_exists="replace", index=False)
        print(f"Loaded {len(df)} rows into '{table}'")


def main() -> None:
    ensure_files_exist()
    with create_connection(DB_PATH) as conn:
        load_tables(conn)
    print(f"Data loaded into {DB_PATH}")


if __name__ == "__main__":
    main()

