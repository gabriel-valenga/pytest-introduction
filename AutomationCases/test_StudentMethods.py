import requests
import json
import jsonpath 

def test_add_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    with open('AddNewStudent.json', 'r') as file:
        json_request = file.read()
    response = requests.post(API_URL, json_request)
    print(response)


def test_get_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/3034"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response,'data.id')
    assert id[0] == 3034


def test_update_student_data():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/3034"
    with open('UpdateStudent.json', 'r') as file:
        json_request = file.read()
    response = requests.put(API_URL, json_request)
    print(response.text)


def test_delete_student():
    API_URL="http://thetestingworldapi.com/api/studentsDetails/3034"
    response = requests.delete(API_URL)
    print(response.text)
