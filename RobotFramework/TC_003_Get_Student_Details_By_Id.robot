*** Settings ***
Library    RequestsLibrary


*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/
${student_id}    28
${response}  
${status_code_as_string}  

*** Test Cases ***
TC_003_Get_Request
    Create Session    GetStudentDetails    ${BASE_URL}
    ${response}    Get Request    GetStudentDetails    api/studentsDetails/${student_id}
    ${status_code_as_string}    Convert To String    ${response.status_code}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Should Be Equal    ${status_code_as_string}    200
