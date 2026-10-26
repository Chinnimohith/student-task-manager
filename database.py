
import sqlite3
from contextlib import contextmanager

DB_NAME = "tasks.db"


@contextmanager
def get_connection():
    conn = sqlite3.connect(DB_NAME)
    try:
        with conn:
            yield conn
    finally:
        conn.close()


def create_table():
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT NOT NULL,
                due_date TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        """)
