*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/


*** Test Cases ***
TC_007 add new student 
    Create Session    addStudent    ${BASE_URL}
    &{body}    Create Dictionary    first_name=Testing    middle_name=A    last_name=World    date_of_birth=12/12/1990
    ${response}    Post Request    addStudent    /api/studentDetails    data=${body}
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}




