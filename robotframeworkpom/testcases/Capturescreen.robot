*** Settings ***
Library     SeleniumLibrary



*** Test Cases ***
LoginTC
    Open Browser    https://demo.nopcommerce.com/      chrome
    Maximize Browser Window
#    Set Selenium Timeout    10
#    Wait Until Page Contains    OrangeHRM
#    Input Text    xpath://input[@name='username']    Admin
#    Input Text    xpath://input[@name='password']    admin123

    Capture Element Screenshot    xpath:/html/body/div[6]/div[1]/div[2]/div[1]/a/img    /Users/surtaram/PycharmProjects/Pytestseleniumpom/robotframeworkpom/logo.png
    Capture Page Screenshot     /Users/surtaram/PycharmProjects/Pytestseleniumpom/robotframeworkpom/page.png



