*** Settings ***
Library  SeleniumLibrary



*** Variables ***
${browser}  chrome
${url}   https://demo.nopcommerce.com/




*** Test Cases ***
LoginTest
#    Create Webdriver    chrome
    Open Browser    ${url}    ${browser}
    Logintoapplication
    Close Browser
    


*** Keywords ***
Logintoapplication
    Click Link    xpath://a[@class='ico-login']
    Input Text    xpath://input[@id='Email']    test@gmail.com
    Input Text    xpath://input[@id='Password']    test@123
    Click Element    xpath://button[@class='button-1 login-button']


