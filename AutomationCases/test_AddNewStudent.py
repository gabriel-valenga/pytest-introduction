import requests
import json
import jsonpath 

def test_add_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    with open('AddNewStudent.json', 'r') as file:
        json_request = file.read()
    response = requests.post(API_URL, json_request)
    print(response)