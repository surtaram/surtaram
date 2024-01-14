*** Settings ***

Library     SeleniumLibrary



*** Variables ***

${url}  https://demo.automationtesting.in/Windows.html
${browser}  chrome



*** Test Cases ***
#Tabbed_windows
#    Open Browser    ${url}  ${browser}
#    Maximize Browser Window
#    Click Element    xpath://*[@id="Tabbed"]/a/button
#    Switch Window   title=

Handle_browser_windows
    Open Browser    https://www.google.com/  ${browser}
    Maximize Browser Window
    Sleep    3


    Open Browser    https://www.bing.com/  ${browser}
    Maximize Browser Window
    Sleep    3

    Switch Browser    1
    ${title1}=   Get Title
    Log To Console    ${title1}


    Switch Browser    2

    ${title2}=   Get Title
    Log To Console    ${title2}

    Close Browser













*** Keywords ***

