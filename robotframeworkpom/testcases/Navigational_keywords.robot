*** Settings ***
Library     SeleniumLibrary


*** Variables ***




*** Test Cases ***
Navigation_Test
    Open Browser    https://www.google.com/     chrome
    ${location}=    Get Location
    Log To Console    ${location}

    Go To    https://www.bing.com/

    ${location}=    Get Location
    Log To Console    ${location}
    Sleep    2
    Go Back
    ${location}=    Get Location
    Log To Console    ${location}
    
    Sleep    2
    
    Close Browser





*** Keywords ***

