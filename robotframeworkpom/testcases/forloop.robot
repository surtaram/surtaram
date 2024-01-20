*** Settings ***


*** Test Cases ***
FORLOOPWITHRANGE
    FOR    ${I}    IN RANGE    0    10  2
        Log To Console  ${I}
         
    END

FORLOOPWITHLIST

    FOR    ${I}    IN    1  2   3   4    5   6  7
        Log To Console   ${I}

    END
    
    
FORLOOPWITHLISTITEAM
    @{ITEMS}=   Create List     1   2   3   4   5
    FOR    ${element}    IN    @{ITEMS}
        Log To Console   ${element}
        Exit For Loop If    ${element}==3
         
    END