# with open("data_test_input_email.csv", 'r', encoding='utf-8') as f:
#     lines = f.readlines()[1:]
# print(lines)
# params = list(map(lambda string: tuple(string.replace('\n', '').split(',')), lines))
# print(params)

def get_test_params():
    with open("data_test_input_email.csv", 'r', encoding='utf-8') as f:
        lines = f.readlines()[1:]
    print(lines)
    for i, line in lines:
        line = line.replace('\n', '')
        lines[i] = tuple(line.split(','))
    print(lines)
    return lines

import pytest
from selenium.webdriver.common.by import By

@pytest.mark.parametrize('email, expected_result, actual_result', get_test_params())
def test_input_email(driver, email, expected_result):
    input_element = driver.find_element(By.NAME, 'form_fields[email]')
    input_element.send_keys(email)
    send_button = driver.find_element(By.CLASS_NAME, "elementor-button elementor-size-md")
    send_button.click()
    assert input_email == expected_result





