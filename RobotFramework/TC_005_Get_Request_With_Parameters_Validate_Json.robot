*** Settings ***
Library    RequestsLibrary
Library    JSONLibrary
Library    Collections

*** Variables ***
${base_url}    https://reqres.in

*** Test Cases ***
TC_005 Validate Get Request With Parameters
    Create Session    Get_Param    ${base_url}
    &{param}    Create Dictionary    page=2
    ${response}    Get Request    Get_Param    /api/users    params=&{param}
    ${status_code}    Convert To String    ${response.status_code}
    Should Be Equal    ${status_code}    200
    ${json_response}    To Json    ${response.content}
    @{name_list}    Get Value From Json    ${json_response}    data[0].first_name
    ${name}    Get Variable Value    @{name_list}    0
    Should Be Equal    ${name}    Hello


