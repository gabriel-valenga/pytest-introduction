import requests
import jsonpath 
import json
import sys 
import os
from openpyxl import load_workbook
from DataDriven import Library


def test_add_mutiple_students():
    API_URL = 'http://thetestingworldapi.com/api/studentsdetails'
    students_data_sheet = Library.ExcelSheet('TestStudentsData.xlsx', 'Planilha1')
    students_data_max_rows = students_data_sheet.fetch_sheet_row_count()
    for i in range(2, students_data_max_rows + 1):
        json_request = students_data_sheet.format_json_request(i)
        response = requests.post(API_URL, json_request) 
        assert response.status_code == 200
      