*** Settings ***
Library     SeleniumLibrary





*** Variables ***
${browser}  chrome
${url}      https://demo.guru99.com/test/newtours/register.php
${email}    test@gmail.com
${password}    test@123


*** Test Cases ***
RegTest
    ${speed}=   Get Selenium Speed
    Log To Console    ${speed}
    Open Browser    ${url}      ${browser}
    Maximize Browser Window
#    Set Selenium Timeout    10
    #Wait Until Page Contains    register    # 5 sec
#    Set Selenium Implicit Wait    10
#    ${defaultimplicitwait}=     Get Selenium Implicit Wait
#    Log To Console    ${defaultimplicitwait}
    Set Selenium Speed    2

    Input Text    xpath://input[@name='firstName']    Ramesh
    Input Text    xpath://input[@name='lastName']    kumar
    Input Text    xpath://input[@name='phone']    78376473672
    Input Text    xpath://input[@name='userName']    ${email}
    Input Text    xpath://input[@name='address1']    xyz 
    Input Text    xpath://input[@name='city']    jaipur
    Input Text    xpath://input[@name='state']    raj
    Input Text    xpath://input[@name='postalCode']    345023
    Select From List By Label    country    AMERICAN SAMOA
    Input Text    xpath://input[@name='email']    ${email}
    Input Text    xpath://input[@name='password']    ${password}
    Input Text    xpath://input[@name='confirmPassword']    ${password}
    Click Element    xpath://input[@name='submit']
    ${speed}=   Get Selenium Speed
    Log To Console    ${speed}

    Close Browser






*** Keywords ***

