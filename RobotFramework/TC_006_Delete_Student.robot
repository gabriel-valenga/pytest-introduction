*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${BASE_URL}    http://thetestingworldapi.com/

*** Test Cases ***
TC_006 Validate Delete Student Request
    Create Session    AppAccess    ${BASE_URL}
    ${response}=    DELETE On Session    AppAccess    api/studentsDetails/28
    Log To Console    ${response.status_code}
    Log To Console    ${response.content}
    ${status_code}=    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    ${json_response}=    To Json    ${response.content}
    ${status_list}=    Get Value From Json    ${json_response}    status
    ${status}=    Get From List    ${status_list}    0
    Should Be Equal    ${status}    true



