import pandas as pd


class ExcelReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read_inventory_file(self):

        df = pd.read_excel(
            self.file_path,
            engine="openpyxl"
        )

        print("\nInventory Data Loaded Successfully!\n")

        print(df)

        return df