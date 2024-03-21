*** Settings ***
Library       Selenium2Library

*** Variables ***
${CurrentURL}            https://calcus.ru/calculator-imt
${Browser}               Chrome
${Calculate}             //input[@value='Рассчитать']
${JS_script}             return document.querySelector('body > div:nth-child(2) > div.columns-container > div.content-column > form > div:nth-child(12) > div.calc-fright > div').textContent
${expect_err_input_h}    return document.querySelector('body > div[2] > div[2] > div[1] > form > div[6] > div[2] > div[1] > div').textContent
${expect_err_input_w}    return document.querySelector('body > div[2] > div[2] > div[1] > form > div[7] > div[2] > div[1] > div').textContent



*** Test Cases ***
Valid_values:
    Calculate    175    87    28.4

Empty_value_h:
    Calculate    ${EMPTY}    87    ${EMPTY}
    ${expect_err_input_h}=    Run Keyword And Expect Error    *    Empty_value_h

Min_value_h:
    Calculate    49    5    ${EMPTY}
    ${expect_err_input_h}=    Run Keyword And Expect Error    *    Min_value_h
    
Max_value_w:
    Calculate    250    501    ${EMPTY}
    ${expect_err_input_w}=    Run Keyword And Expect Error    *    Max_value_w
    
Not_int_h:
    Calculate    H    70    ${EMPTY}
    ${expect_err_input_h}=    Run Keyword And Expect Error    *    Not_int_h
    Close Browser

*** Keywords ***
Calculate
    [Arguments]    ${height}    ${weight}    ${result}

    Open Browser    ${CurrentURL}    ${Browser}
    Maximize Browser Window

        Input Text    height    ${height}
        Input Text    weight    ${weight}
        Click Button            ${Calculate}
        Sleep    3
        ${result-row}=    Execute JavaScript   ${JS_script}
        Should Be Equal As Strings  ${result}  ${result-row}