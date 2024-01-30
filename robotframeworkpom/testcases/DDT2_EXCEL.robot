*** Settings ***
Library     SeleniumLibrary
Resource    ../Resourses/login_resourses.robot
Library     DataDriver      ../Testdata/data_driven.xlsx    sheet_name=Sheet1

Suite Setup     Open my browser
Suite Teardown      close browsers

Test Template   Invalid Login





*** Test Cases ***
Login Test with excel using   ${username}    ${password}







*** Keywords ***
Invalid Login
    [Arguments]     ${username}     ${password}
    Input username    ${username}
    Input pwd       ${password}
    Click Login Button
    Error message should be visible







