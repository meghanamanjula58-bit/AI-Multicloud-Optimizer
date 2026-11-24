
import sqlite3
import pandas as pd

DB_NAME = "cloud_database.db"

def initialize_database():

    conn = sqlite3.connect(DB_NAME)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS cloud_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Cloud TEXT,
            Resource TEXT,
            CPU REAL,
            Memory REAL,
            Storage REAL,
            Cost REAL,
            Status TEXT,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def save_cloud_data(data):

    conn = sqlite3.connect(DB_NAME)

    data.to_sql(
        "cloud_history",
        conn,
        if_exists="append",
        index=False
    )

    conn.close()


def get_cloud_history():

    conn = sqlite3.connect(DB_NAME)

    history = pd.read_sql_query(
        "SELECT * FROM cloud_history ORDER BY id DESC",
        conn
    )

    conn.close()

    return history
