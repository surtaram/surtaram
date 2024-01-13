*** Settings ***
Library     SeleniumLibrary





*** Variables ***
${browser}  chrome
${url}  https://demo.guru99.com/test/radio.html




*** Test Cases ***
Radio_button
    Open Browser    ${url}  ${browser}
    Maximize Browser Window
    Select Radio Button    webform    Option 1
    @{checkboxes}=  Create List     checkbox1   checkbox2   checkbox3
    FOR    ${checkbox}    IN    @{checkboxes}
        Select Checkbox    ${checkbox}
     END
     Sleep    3
     FOR    ${checkbox}    IN    @{checkboxes}
         Log    ${checkbox}
         Unselect Checkbox    ${checkbox}
          
     END
     Sleep    5
#    Select Checkbox    //input[@value='checkbox1']
#    \   

    Close Browser






*** Keywords ***



