import requests
import jsonpath 
import json
from openpyxl import load_workbook

def test_add_mutiple_students():
    API_URL = 'http://thetestingworldapi.com/api/studentsdetails'
    students_data = load_workbook('TestStudentsData.xlsx')
    students_data_sheet = students_data['Planilha1']
    students_data_max_rows = students_data_sheet.max_row
    for i in range(2, students_data_max_rows + 1):
        cell_first_name = students_data_sheet.cell(row=i, column=1)
        cell_middle_name = students_data_sheet.cell(row=i, column=2)
        cell_last_name = students_data_sheet.cell(row=i, column=3)
        cell_date_of_birth = students_data_sheet.cell(row=i, column=4)
        json_request = {"first_name": cell_first_name.value,
                         "middle_name": cell_middle_name.value,
                         "last_name": cell_last_name.value,
                         "date_of_birth": cell_date_of_birth.value.strftime('%Y-%m-%d')}
        response = requests.post(API_URL, json_request) 
        assert response.status_code == 200
      