*** Settings ***


Library     SeleniumLibrary
Resource    ../Resourses/Resourses.robot

*** Test Cases ***
TC1
    #without argument user defined keyword
    ${application_Title}=    LaunchBrowser   ${url}    ${browser}
    Log To Console    ${application_Title}
    Input Text    xpath://input[@name='userName']    mercury
    Input Text    xpath://input[@name='password']    mercury



*** Variables ***
${url}  https://demo.guru99.com/test/newtours/login.php
${browser}  chrome



