*** Settings ***

Suite Setup     Log To Console    opening browser
Suite Teardown      Log To Console    Closing browser

Test Setup      Log To Console    Loging into application
Test Teardown   Log To Console    Logout from application




*** Test Cases ***
TC1 Prepaid Recharge
    Log To Console    this is prepaid recharge test case
TC2 Postpaid recharge
    Log To Console    Postpaid recharge test case

TC3 Search Test case
    Log To Console    This is search test cases

TC4 Advanced search functionality
    Log To Console    Advanced search test cases
