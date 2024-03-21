import requests
import json
import jsonpath 
from http import HTTPStatus

student_id = ''

def test_add_student_data():
    global student_id
    API_URL="http://thetestingworldapi.com/api/studentsDetails"
    with open(r'AddNewStudent.json', 'r') as file:
        json_request = file.read()
    response = requests.post(API_URL, json_request)
    student = json.loads(response.text)
    student_id = jsonpath.jsonpath(student[0], 'id')[0]
    print(student_id)
    assert response.status_code == HTTPStatus.CREATED



def test_get_student_data():
    global student_id
    API_URL= f"http://thetestingworldapi.com/api/studentsDetails/{student_id}"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response,'data.id')[0]
    assert response.status_code == HTTPStatus.OK


def test_update_student_data():
    global student_id
    API_URL=f"http://thetestingworldapi.com/api/studentsDetails/{student_id}"
    with open(r'UpdateStudent.json', 'r') as file:
        json_request = file.read()
    response = requests.put(API_URL, json_request)
    assert response.status_code == HTTPStatus.OK


def test_delete_student():
    global student_id
    API_URL=f"http://thetestingworldapi.com/api/studentsDetails/{student_id}"
    response = requests.delete(API_URL)
    assert response.status_code == HTTPStatus.NO_CONTENT


def test_add_student_tech_details():
    global student_id
    API_URL = f"http://thetestingworldapi.com/api/technicalskills/{student_id}"
    with open(r'StudentTechDetailsData.json', 'r') as file:
        request_json = json.loads(file.read())
    response = requests.put(API_URL, request_json)
    print(response.text)
    assert response.status_code == HTTPStatus.OK

    
def test_add_student_addresses():
    global student_id
    API_URL = f"http://thetestingworldapi.com/api/adresses/{student_id}"
    with open(r'StudentAdresses.json', 'r') as file:
        request_json = json.loads(file.read())
    response = requests.post(API_URL, request_json)
    print(response.text)
    assert response.status_code == HTTPStatus.OK


def test_get_student_final_details():
    global student_id
    API_URL = f"http://thetestingworldapi.com/api/FinalStudentDetails/{student_id}"
    response = requests.get(API_URL)
    print(response.text)
    assert response.status_code == HTTPStatus.OK


