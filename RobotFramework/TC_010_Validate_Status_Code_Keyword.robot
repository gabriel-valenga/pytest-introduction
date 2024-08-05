*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections
Resource   Resources/UserKeyword.robot
Suite Setup    Test Begin
Suite Teardown    Test End


*** Variables ***
${base_url}    http://thetestingworldapi.com/


*** Test Cases ***
TC_010_Fetch_Student_Details_By_Id
    [Documentation]    This testcase is for fetch student details by Id
    [Timeout]    1s
    [Setup]    Test Begin
    [Teardown]    Test End
    Fetch and Validate Get Status Code    50    200
    ${response}    Fetch and Return Get Response    50
    Log To Console    ${response.content}
