import schedule
import time

from modules.database import InventoryDB
from modules.alerts import AlertManager


def check_low_stock():

    db = InventoryDB()

    records = db.get_inventory_data()

    alert_manager = AlertManager()

    for row in records:

        product_id = row[0]
        product_name = row[1]
        reorder_point = row[4]
        quantity_on_hand = row[6]

        if quantity_on_hand < reorder_point:

            message = (
                f"ALERT! {product_name} stock is low. "
                f"Current stock: {quantity_on_hand}"
            )

            print(message)

            alert_data = (
                product_id,
                "LOW_STOCK",
                "WARNING",
                message
            )

            db.insert_alert(alert_data)

            # SEND EMAIL
            alert_manager.send_email_alert(
                "Inventory Low Stock Alert",
                message
            )

    db.close()


schedule.every(10).seconds.do(check_low_stock)

print("Tracker Running...")

while True:

    schedule.run_pending()

    time.sleep(1)