import json

def read_request_content():
    with open('RobotFramework\ReadContent\Request.json') as file:
        json_file = file.read()
        json_content = json.load(json_file)
        return json_content
