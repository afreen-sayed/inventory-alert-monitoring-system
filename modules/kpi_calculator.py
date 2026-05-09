import pandas as pd


class KPICalculator:

    def calculate_inventory_value(self, qty, unit_cost):

        return qty * unit_cost

    def calculate_stock_status(self, qty, min_stock, reorder_point):

        if qty < min_stock:
            return "CRITICAL"

        elif qty < reorder_point:
            return "LOW"

        else:
            return "OK"