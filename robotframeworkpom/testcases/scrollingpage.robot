*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***

ScrollingTest
    Open Browser    https://www.countries-ofthe-world.com/flags-of-the-world.html   chrome
    Maximize Browser Window
    Sleep    2
    Execute Javascript  window.scrollTo(0,1500)
    Sleep    2

    Close Browser
ScrollPageTillelementfound
    Open Browser    https://www.countries-ofthe-world.com/flags-of-the-world.html   chrome
    Maximize Browser Window
    Sleep    2
    Scroll Element Into View    xpath://*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[2]
    Sleep    2
    Close Browser
ScrollTillBottom
    Open Browser    https://www.countries-ofthe-world.com/flags-of-the-world.html   chrome
    Maximize Browser Window
    Sleep    2
    #end of the page
    Execute Javascript      window.scrollTo(0,document.body.scrollHeight)
    Sleep    2
    #again comback to top of the page
    Execute Javascript      window.scrollTo(0,-document.body.scrollHeight)
    Sleep    2

    Close Browser
