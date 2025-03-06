import sqlite3
conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS orders (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         user TEXT NOT NULL,
#         order_details TEXT NOT NULL,
#         status TEXT DEFAULT 'pending'
#     )
# """)
# conn.commit()

# cursor.execute("ALTER TABLE orders ADD COLUMN DATE_TIME DEFAULT '01/01/2025,05:30'")
# conn.commit()


cursor.execute("SELECT * FROM orders")
orders = cursor.fetchall()

for order in orders:
    print(order)


conn.close()