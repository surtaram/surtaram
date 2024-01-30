*** Settings ***



*** Test Cases ***

TC1 User registration Test
    [Tags]  regression
    Log To Console    This is user reg test
    Log To Console    user reg test is over

TC2 Login test
    [Tags]  sanity
    Log To Console    This is login test
    Log To Console    Login test is over

TC3 Change user setting
    [Tags]  regression
    Log To Console    Change user setting test case
    Log To Console    User setting changed successfully

TC4 Logout test
    [Tags]  sanity
    Log To Console    This is logout test
    Log To Console    Logout test is over


