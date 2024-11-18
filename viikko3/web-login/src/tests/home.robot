*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application And Go To Starting Page


*** Variables ***
${SERVER}        localhost:5001
${DELAY}         0.5 seconds
${HOME_URL}      http://${SERVER}

*** Test Cases ***
Click Login Link
    Click Link  Login
    Title Should Be  Login

Click Register Link
    Click Link  Register new user
    Title Should Be  Register

*** Keywords ***

Reset Application And Go To Starting Page
  Reset Application
  Go To  ${HOME_URL}
