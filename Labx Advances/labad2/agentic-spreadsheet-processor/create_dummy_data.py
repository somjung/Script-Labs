# create_dummy_data.py
# Creates the sample input file for the agentic spreadsheet processor.
# (The lab doc says input_data.xlsx is created "manually or by another
# script" - this is that script.)
import os
import openpyxl

def main():
    os.makedirs("data", exist_ok=True)
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "SalesData"
    rows = [
        ["Product Name", "Quantity", "Unit Price"],
        ["Laptop", 2, 1200.50],
        ["Mouse", 5, 25.00],
        ["Keyboard", 3, 75.99],
        ["Monitor", 1, 300.00],
        ["Projector", 1, 850.00],
        ["Webcam", 10, 45.00],
        ["Headset", 4, 99.99],
        ["SSD", 2, 180.00],
        ["Router", 1, 70.00],
    ]
    for row in rows:
        ws.append(row)
    wb.save("data/input_data.xlsx")
    print("data/input_data.xlsx created")

if __name__ == "__main__":
    main()
