*** Settings ***
Library     SeleniumLibrary

*** Variables ***

${url}      https://demo.guru99.com/test/newtours/register.php
${browser}      chrome

*** Test Cases ***
Drop_down_handle
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Select From List By Label    country    ALBANIA
    Sleep    2
    Select From List By Index    country    1
    Sleep    3
    Select From List By Value    country    AMERICAN SAMOA
    Sleep    4
    Close Browser
List_box_handle
    Open Browser    ${url}  ${browser}
    Maximize Browser Window




*** Keywords ***




