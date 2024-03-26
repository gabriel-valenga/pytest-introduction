import json
import jsonpath
from openpyxl import load_workbook

class ExcelSheet:

    def __init__(self, fileNamePath, SheetName):
        global workbook
        global sheet
        workbook = load_workbook(fileNamePath)
        sheet = workbook[SheetName]

    def fetch_sheet_row_count(self):
        return sheet.max_row
    

    def fetch_sheet_column_count(self):
        return sheet.max_column
