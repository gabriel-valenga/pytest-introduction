*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/


*** Test Cases ***
TC_008 update student 
    Create Session    updateStudent    ${BASE_URL}
    &{body}    Create Dictionary    id=1818 first_name=Testing    middle_name=Update    last_name=World    date_of_birth=12/12/1990
    &{header}    Create Dictionary    Content-Type=application/json
    ${response}    Put Request    updateStudent    /api/studentDetails/1818    data=${body}    headers=${header}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    Should Be Equal    ${response.status_code}    201




