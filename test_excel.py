from modules.excel_reader import ExcelReader


reader = ExcelReader("data/sample_inventory.xlsx")


df = reader.read_inventory_file()