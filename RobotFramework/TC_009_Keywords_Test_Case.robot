*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/

# To reuse the code multiple times in the same file
*** Keywords ***
Get Student Details 
    [Arguments]    ${studentId}
    Create Session    GetStudentDetails    ${BASE_URL}
    ${response}    Get Request    GetStudentDetails    api/studentsDetails/${student_id}
    ${status_code_as_string}    Convert To String    ${response.status_code}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Should Be Equal    ${status_code_as_string}    200



*** Test Cases ***
TC_009 add new student and then get new student added
    [Tags]    TagA
    Create Session    addStudent    ${BASE_URL}
    &{body}    Create Dictionary    first_name=Testing    middle_name=A    last_name=World    date_of_birth=12/12/1990
    &{header}    Create Dictionary    Content-Type=application/json
    ${response}    Post Request    addStudent    /api/studentDetails    data=${body}    headers=${header}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Should Be Equal    ${response.status_code}    201
    ${json_response}    To Json    ${response.content}
    ${id_list}    Get Value From Json    ${json_response}    id
    ${student_id}    Get From List    ${id_list}    0
    Get Student Details    ${student_id}    


