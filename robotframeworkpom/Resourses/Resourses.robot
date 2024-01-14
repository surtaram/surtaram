*** Settings ***

Library     SeleniumLibrary


*** Keywords ***

LaunchBrowser
    [Arguments]     ${appurl}    ${appbrowser}
    Open Browser    ${appurl}  ${appbrowser}
    Maximize Browser Window
    ${title}=   Get Title
#    Log To Console     ${title}
    [RETURN]    ${title}