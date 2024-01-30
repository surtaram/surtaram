*** Settings ***

Library     SeleniumLibrary


*** Variables ***
${URL}      https://demo.nopcommerce.com/login?returnUrl=%2F
${browser}      chrome


*** Keywords ***

Open my browser
    Open Browser    ${URL}      ${browser}
    Maximize Browser Window
close browsers
    Close All Browsers
Open Login Page
    Go To    ${URL}
Input username
    [Arguments]     ${username}
    Input Text    id:Email    ${username}
Input pwd
    [Arguments]     ${password}
    Input Text    id:Password     ${password}
Click Login Button
    Click Element    xpath://button[@class='button-1 login-button']
Click Logout link
    Click Link    Logout
Error message should be visible
    Page Should Contain    Login was unsuccessful.
Dashboard page should be visible
    Page Should Contain    Dashboard


