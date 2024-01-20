*** Settings ***


Library     SeleniumLibrary

*** Test Cases ***

Getalllinks
    Open Browser    https://demo.guru99.com/test/newtours/register.php      chrome
    Maximize Browser Window

    ${AllLinkCount}=    Get Element Count    xpath://a
    Log To Console    ${AllLinkCount}

    ${LinkItem}     Create List
    FOR    ${I}    IN RANGE    1    ${AllLinkCount}
        ${LinkText}=    Get Text    xpath:(//a)[${I}]
        Log To Console   ${LinkText}

    END

    Close Browser