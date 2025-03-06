import sqlite3
from config import DB_PATH

def get_db_connection():
    """Establish SQLite database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Return results as dictionaries
    return conn

def initialize_db():
    """Creates the necessary tables if they do not exist."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            order_details TEXT,
            status TEXT DEFAULT 'pending'
        )
        """
        )
        conn.commit()

# Initialize database on import
initialize_db()
