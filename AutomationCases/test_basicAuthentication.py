import json
import requests
from requests.auth import HTTPBasicAuth
from http import HTTPStatus

def test_with_authentication():
    with open('Authentication.json', 'r')  as file:
        authentication_json_file = json.load(file)
        username = authentication_json_file['username']
        password = authentication_json_file['password']
        response = requests.get(url='http://thetestingworldapi.com/Account/ExternalLogin', auth=HTTPBasicAuth(username=username, password=password))
        assert response.status_code == HTTPStatus.OK

