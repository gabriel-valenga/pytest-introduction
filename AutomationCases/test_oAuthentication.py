import json
import requests 
import jsonpath

def test_oauth_api():
    TOKEN_URL = 'http://thetestingworldapi.com/Token'
    data = {'grant_type': 'password', 'username': 'admin'}
    response = requests.post(TOKEN_URL, data)
    token_value = jsonpath.jsonpath(response.json(), 'access_token')
    auth = {'Authorization': f'Bearer {token_value[0]}'}
    API_URL = 'http://thetestingworldapi.com/api/stdetails/1104'
    response = requests.get(API_URL, headers=auth)
    print(response.text)
