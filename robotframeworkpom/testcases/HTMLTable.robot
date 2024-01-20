*** Settings ***
Library     SeleniumLibrary



*** Test Cases ***

HTMLTable_handle
    Open Browser        https://testautomationpractice.blogspot.com/    chrome
    Maximize Browser Window
    ${Number_of_rows}=  Get Element Count    xpath://table[@name="BookTable"]/tbody/tr
    Log To Console    ${Number_of_rows}
    ${Number_of_column}=    Get Element Count    xpath://table[@name="BookTable"]/tbody/tr[1]/th
    Log To Console     ${Number_of_column}
    
    ${data}=    Get Text    xpath://table[@name="BookTable"]/tbody/tr[5]/td[1]
    
    FOR    ${i}    IN RANGE    1    ${Number_of_column}+1
        ${Table_header}=    Get Text    xpath://table[@name="BookTable"]/tbody/tr[1]/th[${i}]
        Log To Console  ${Table_header}
    END

    FOR    ${I}    IN RANGE    2    ${Number_of_rows}+1
        FOR    ${J}    IN RANGE    1     ${Number_of_column}+1
                ${Table_data}=  Get Text    xpath://table[@name="BookTable"]/tbody/tr[${I}]/td[${J}]
                Log To Console    ${Table_data}
        END
    END
    
    Table Column Should Contain    xpath://table[@name="BookTable"]    2    Author
    Table Row Should Contain    xpath://table[@name="BookTable"]    4    Learn JS
    Table Cell Should Contain    xpath://table[@name="BookTable"]    5    2    Mukesh
    Table Header Should Contain    xpath://table[@name="BookTable"]    BookName


    Log To Console    ${data}
    Log To Console    ${Number_of_rows}
    Log To Console     ${Number_of_column}

    


    Close Browser

    





