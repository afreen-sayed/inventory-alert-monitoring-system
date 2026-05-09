import sqlite3
from config import DB_PATH


class InventoryDB:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cursor = self.conn.cursor()

    # CREATE PRODUCTS TABLE
    def create_products_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            product_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            category TEXT,
            unit_cost REAL,
            reorder_point INTEGER,
            max_stock INTEGER,
            min_stock INTEGER,
            supplier TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """

        self.cursor.execute(query)

        self.conn.commit()

    # CREATE INVENTORY TABLE
    def create_inventory_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS inventory_levels (
            id INTEGER PRIMARY KEY,
            product_id TEXT NOT NULL,
            date TEXT NOT NULL,
            quantity_on_hand INTEGER,
            quantity_reserved INTEGER,
            quantity_available INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(product_id)
            REFERENCES products(product_id)
        )
        """

        self.cursor.execute(query)

        self.conn.commit()

    # CREATE ALERTS TABLE
    def create_alerts_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY,
            product_id TEXT NOT NULL,
            alert_type TEXT,
            severity TEXT,
            message TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY(product_id)
            REFERENCES products(product_id)
        )
        """

        self.cursor.execute(query)

        self.conn.commit()

    # INSERT PRODUCT
    def insert_product(self, product_data):

        query = """
        INSERT OR IGNORE INTO products (
            product_id,
            name,
            category,
            unit_cost,
            reorder_point,
            max_stock,
            min_stock,
            supplier
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        self.cursor.execute(query, product_data)

        self.conn.commit()

    # INSERT INVENTORY LEVEL
    def insert_inventory_level(self, inventory_data):

        query = """
        INSERT INTO inventory_levels (
            product_id,
            date,
            quantity_on_hand,
            quantity_reserved,
            quantity_available
        )
        VALUES (?, ?, ?, ?, ?)
        """

        self.cursor.execute(query, inventory_data)

        self.conn.commit()

    # INSERT ALERT
    def insert_alert(self, alert_data):

        query = """
        INSERT INTO alerts (
            product_id,
            alert_type,
            severity,
            message
        )
        VALUES (?, ?, ?, ?)
        """

        self.cursor.execute(query, alert_data)

        self.conn.commit()

    # GET INVENTORY DATA
    def get_inventory_data(self):

        query = """
        SELECT
            p.product_id,
            p.name,
            p.category,
            p.unit_cost,
            p.reorder_point,
            p.min_stock,
            i.quantity_on_hand,
            i.quantity_reserved,
            i.quantity_available

        FROM products p

        JOIN inventory_levels i
        ON p.product_id = i.product_id
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # GET ALERTS
    def get_alerts(self):

        query = """
        SELECT * FROM alerts
        ORDER BY created_at DESC
        """

        self.cursor.execute(query)

        return self.cursor.fetchall()

    # CLOSE CONNECTION
    def close(self):

        self.conn.close()
        