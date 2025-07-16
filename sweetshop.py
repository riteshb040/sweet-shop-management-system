import sqlite3

class SweetShop:
    def __init__(self, db_name="sweetshop.db"):
        # Set database name and create the table if not exists
        self.db_name = db_name
        self.create_table()

    def connect(self):
        # Connect to SQLite database
        return sqlite3.connect(self.db_name)

    def create_table(self):
        # Create the sweets table with required fields
        with self.connect() as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS sweets (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    category TEXT,
                    price REAL,
                    quantity INTEGER
                )
            ''')

    def add_sweet(self, id, name, category, price, quantity):
        # Add or update a sweet using its ID
        with self.connect() as conn:
            conn.execute('''
                INSERT OR REPLACE INTO sweets (id, name, category, price, quantity)
                VALUES (?, ?, ?, ?, ?)
            ''', (id, name, category, price, quantity))

    def delete_sweet(self, id):
        # Delete sweet by ID
        with self.connect() as conn:
            conn.execute("DELETE FROM sweets WHERE id = ?", (id,))

    def view_all_sweets(self):
        # Show all sweets in the inventory
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * FROM sweets")
            rows = cur.fetchall()
            return [
                {"id": row[0], "name": row[1], "category": row[2], "price": row[3], "quantity": row[4]}
                for row in rows
            ]

    def search_sweets(self, name=None, category=None, min_price=None, max_price=None):
        # Search sweets by name, category or price range
        query = "SELECT * FROM sweets WHERE 1=1"
        params = []

        if name:
            query += " AND LOWER(name) = ?"
            params.append(name.lower())
        if category:
            query += " AND LOWER(category) = ?"
            params.append(category.lower())
        if min_price is not None:
            query += " AND price >= ?"
            params.append(min_price)
        if max_price is not None:
            query += " AND price <= ?"
            params.append(max_price)

        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(query, params)
            rows = cur.fetchall()
            return [
                {"id": row[0], "name": row[1], "category": row[2], "price": row[3], "quantity": row[4]}
                for row in rows
            ]

    def purchase_sweet(self, id, quantity):
        # Reduce quantity when sweet is purchased
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT quantity FROM sweets WHERE id = ?", (id,))
            result = cur.fetchone()

            if not result:
                raise ValueError("Sweet not found.")
            if result[0] < quantity:
                raise ValueError("Not enough stock available")

            conn.execute("UPDATE sweets SET quantity = quantity - ? WHERE id = ?", (quantity, id))

    def restock_sweet(self, id, quantity):
        # Increase stock quantity of a sweet
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT id FROM sweets WHERE id = ?", (id,))
            if not cur.fetchone():
                raise ValueError("Sweet not found.")
            conn.execute("UPDATE sweets SET quantity = quantity + ? WHERE id = ?", (quantity, id))

    def sort_sweets(self, sort_by="name"):
        # Sort sweets by name, category, price, or quantity
        if sort_by not in ["name", "category", "price", "quantity"]:
            raise ValueError("Invalid sort key. Choose from name, category, price, quantity.")

        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT * FROM sweets ORDER BY {sort_by}")
            rows = cur.fetchall()
            return {
                row[0]: {
                    "name": row[1],
                    "category": row[2],
                    "price": row[3],
                    "quantity": row[4]
                }
                for row in rows
            }

    def clear_all(self):
        # Clear all sweets (used for testing or reset)
        with self.connect() as conn:
            conn.execute("DELETE FROM sweets")
