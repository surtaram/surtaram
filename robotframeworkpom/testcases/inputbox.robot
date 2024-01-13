*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://demo.nopcommerce.com/



*** Test Cases ***
TestingInputBox
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Title Should Be    nopCommerce demo store
    Click Link    xpath://a[@class='ico-login']
    ${"email_txt"}  Set Variable     xpath://input[@id='Email']
    Element Should Be Visible    ${"email_txt"}
    Element Should Be Enabled    ${"email_txt"}
    Input Text    ${"email_txt"}    test@gmail.com
    Sleep    5
    Clear Element Text    ${"email_txt"}
    Sleep    3
    Close Browser


#    Input Text    xpath://input[@id='Email']    test@gmail.com
#    Input Text    xpath://input[@id='Password']    test@123
#    Click Element    xpath://button[@class='button-1 login-button']
#    Close Browser



*** Keywords ***


