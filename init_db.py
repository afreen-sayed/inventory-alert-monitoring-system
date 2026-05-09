from modules.database import InventoryDB


db = InventoryDB()


db.create_products_table()
db.create_inventory_table()
db.create_alerts_table()

print("Database initialized successfully!")


db.close()