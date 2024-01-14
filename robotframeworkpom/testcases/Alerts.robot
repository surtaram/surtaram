*** Settings ***
Library     SeleniumLibrary



*** Variables ***

${browser}     chrome
${url}      https://testautomationpractice.blogspot.com/



*** Test Cases ***
Alerts_handle
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Click Element    xpath://button[@onclick='myFunctionAlert()']
    Sleep    3
    Handle Alert    Accept
    Click Element    xpath://button[@onclick='myFunctionConfirm()']
    Sleep    3
#    Handle Alert    Dismiss
#    Handle Alert    Leave     # this will use for keep alert on screen
    Alert Should Not Be Present    Press a button!
    #this keyword use for checking alerts are present or not
    Sleep    2
    Close Browser

Frames_handle
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    #1st frame
    Select Frame    locator
    Click Link    locator
    Unselect Frame
#    2nd frame
    Select Frame    locator
    Click Link    locator
    Unselect Frame

    Close Browser







