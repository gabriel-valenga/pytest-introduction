*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Resource   Resources/UserKeyword.robot


*** Variables ***
${base_url}    http://thetestingworldapi.com/


*** Test Cases ***
TC_010_Fetch_Student_Details_By_Id
    Fetch and Validate Get Status Code    50    200
    ${response}    Fetch and Return Get Response    50
    Log To Console    ${response.content}
