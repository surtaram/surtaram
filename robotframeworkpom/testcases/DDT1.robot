*** Settings ***

Library     SeleniumLibrary
Resource    ../Resourses/login_resourses.robot

Suite Setup     Open my browser
Suite Teardown      close browsers
Test Template   Invalid login

*** Test Cases ***  username    password
Right user empty password   admin@yourstore.com     ${EMPTY}
Right user and wrong pass   admin@yourstore.com     xyz
Wrong user and right pass   test@gmail.com      admin
wrong user and wrong pass   test@gmail.com      xys









*** Keywords ***
Invalid login
    [Arguments]     ${username}     ${password}
    Input username  ${username}
    Input pwd   ${password}
    Click Login Button
    Error message should be visible


