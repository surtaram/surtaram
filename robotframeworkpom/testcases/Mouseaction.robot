*** Settings ***

Library     SeleniumLibrary


*** Test Cases ***

MouseAction
    #Right click action
#    Open Browser    url=        browser=chrome
#    Maximize Browser Window
#
#    Open Context Menu    locator
#    Sleep    2

    #Double click action
    Open Browser    https://testautomationpractice.blogspot.com/    chrome
    Maximize Browser Window

#    Double Click Element    xpath://*[@id="HTML10"]/div[1]/button
#    Sleep    2
    #Drag and drop
    Drag And Drop    xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[5]/div[1]/div[1]/p    xpath:/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[5]/div[1]/div[2]
    Sleep    5
    Close Browser

