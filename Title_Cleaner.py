from openpyxl import Workbook, load_workbook
""" Work Book """
wb = load_workbook("Titles.xlsx")
ws = wb.active


ws["C40"] = "66"
wb.save("Titles.xlsx")