import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize(
    "name, expected_result, actual_result",
    [
        ("Anna", "Anna", "Anna"),
        ("Анна", "Анна", "Анна"),
        (None, "Вы пропустили это поле", "Вы пропустили это поле"),
        ("###", "Поле имя не может содержать только спецсимволы", "Поле имя не может содержать только спецсимволы"),
    ]
)
def test_input_name(driver, name, expected_result, actual_result):
    input_name = driver.find_element(By.ID, "form-field-name")
    input_name.send_keys(name)
    send_button = driver.find_element(By.CLASS_NAME, "elementor-button elementor-size-md")
    send_button.click()
    # код для поп-апа с error-message
    assert input_name() == expected_result



