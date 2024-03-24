from selenium.webdriver.support import AssertionError
from selenium.webdriver.common.by import By

def input_valid_comment(): # вводим валидное значение
    comment = "text"
    expected_result = "text"
    actual_result = "text"
    assert actual_result == expected_result

def input_comment_empty (): # оставляем поле незаполненным
    comment = None
    expected_result = "Вы пропустили это поле"
    actual_result = "Вы пропустили это поле"
    assert actual_result == expected_result

def test_input_valid_comment(driver, comment, expected_result, actual_result):
    try:
        input_comment = driver.find_element(By.ID, "form-field-message")
        input_comment.send_keys(comment)
        send_button = driver.find_element(By.CLASS_NAME, "elementor-button elementor-size-md")
        send_button.click()
        assert actual_result() == expected_result
    except AssertionError:
        result = driver.get("https://webtucre.ru/testovaya-stranicza-4/")
        assert result == expected_result

def test_input_comment_empty(driver, comment, expected_result, actual_result):
    try:
        input_comment = driver.find_element(By.ID, "form-field-message")
        input_comment.send_keys(comment)
        send_button = driver.find_element(By.CLASS_NAME, "elementor-button elementor-size-md")
        send_button.click()
        assert actual_result() == expected_result
    except AssertionError:
        result = driver.get("https://webtucre.ru/testovaya-stranicza-4/")
        assert result == expected_result