*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections


*** Variables ***
${base_url}    http://thetestingworldapi.com/

*** Keywords ***
Fetch and Validate Get Status Code
    [Arguments]    ${studentId}    ${expectedStatusCode}
    Create Session    SessionName    ${base_url}
    ${response}    Get Request    SessionName    api/studentDetails/{studentId}
    ${statusCode}    Convert To String    ${response.status_code}  
    Should Be Equal    ${statusCode}    ${expectedStatusCode}    


Fetch and Return Get Response
    [Arguments]    ${studentId}
    Create Session    SessionName    ${base_url}
    ${response}    Get Request    SessionName    api/studentDetails/{studentId}
    [Return]    ${response} 