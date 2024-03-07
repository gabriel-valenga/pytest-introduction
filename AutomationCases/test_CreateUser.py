import requests
import json 
import jsonpath
import pytest

#API URL
url = 'https://reqres.in/api/users'
a = 100
json_input = ''

@pytest.fixture
def start_and_finish_execution():
    #Read input JSON file
    global json_input
    with open('CreateUser.json', 'r') as file:
        json_input = file.read()
    yield 
    print('test case finished!')


@pytest.mark.skipif(a>100, reason='Condition is not satisfied')
def test_create_new_user(start_and_finish_execution):
    global json_input
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201 #validating response code
    print(response.headers.get('Content-Length')) #fetch header from Response
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])


def test_create_other_user(start_and_finish_execution):
    global json_input
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    assert response.status_code == 201 #validating response code
    print(response.headers.get('Content-Length')) #fetch header from Response
    response_json = json.loads(response.text)
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])