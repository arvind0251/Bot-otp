import sqlite3
from config import DB_NAME

def db_connect():
    conn = sqlite3.connect(DB_NAME, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            balance REAL
        )
    """)
    conn.commit()
    return conn
