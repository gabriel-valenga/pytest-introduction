*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/
${response}


*** Test Cases ***
TC_001_Get_Request
    Create Session    GetStudentDetails    ${BASE_URL}
    ${response}    Get Request    GetStudentDetails    api/studentsDetails
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
