from datetime import datetime

from modules.excel_reader import ExcelReader
from modules.database import InventoryDB


reader = ExcelReader("data/sample_inventory.xlsx")


df = reader.read_inventory_file()


db = InventoryDB()


for _, row in df.iterrows():

    product_data = (
        row["product_id"],
        row["name"],
        row["category"],
        row["unit_cost"],
        row["reorder_point"],
        row["max_stock"],
        row["min_stock"],
        row["supplier"]
    )

    db.insert_product(product_data)

    quantity_available = (
        row["quantity_on_hand"]
        - row["quantity_reserved"]
    )

    inventory_data = (
        row["product_id"],
        datetime.now().strftime("%Y-%m-%d"),
        row["quantity_on_hand"],
        row["quantity_reserved"],
        quantity_available
    )

    db.insert_inventory_level(inventory_data)


print("\nData loaded into database successfully!")


db.close()