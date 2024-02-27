import requests
import json 
import jsonpath

#API URL
url = 'https://reqres.in/api/users'

def test_create_new_user():
    #Read input JSON file
    with open('CreateUser.json', 'r') as file:
        json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201 #validating response code
    print(response.headers.get('Content-Length')) #fetch header from Response
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

def test_create_other_user():
    #Read input JSON file
    with open('CreateUser.json', 'r') as file:
        json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 202 #validating response code
    print(response.headers.get('Content-Length')) #fetch header from Response
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

test_create_new_user()
test_create_other_user()