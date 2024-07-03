*** Settings ***

Library    RequestsLibrary

*** Variables ***
${Application_URL}    http://www.thetestingworldapi.com

*** Test Cases ***
TC_001_Get_Request
    ${url}    Set Variable    HelloWorld
    Log To Console    ${Application_URL}
    Log To Console    ${url}

# $ to store common variables
# @ to store list variables 
# & to store dict variables
