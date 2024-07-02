*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections


*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/
${student_id}    28
${response}  
${status_code_as_string}  
${json_response}
${first_name_list}
${first_name}

*** Test Cases ***
TC_003_Get_Request
    Create Session    GetStudentDetails    ${BASE_URL}
    ${response}    Get Request    GetStudentDetails    api/studentsDetails/${student_id}  
    ${status_code_as_string}    Convert To String    ${response.status_code}
    Log To Console    ${response.json()}
    ${json_response}    Get Variable Value    ${response.json()}    
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    ${first_name_list}    Get Value From Json    ${json_response}    data.first_name
    ${first_name}    Get From List    ${first_name_list}    0
    Log To Console    ${first_name}
    Should Be Equal    ${first_name}    Test Student
