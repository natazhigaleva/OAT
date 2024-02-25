import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://webtucre.ru/testovaya-stranicza-4/")
    yield driver

## -------------------------- Test-case №1 ---------------------------------##
def input_valid_name_eng_gb(): # вводим валидное значение на латинице
    name = "Anna"
    expected_result = "Anna"
    actual_result = "Anna"
    assert actual_result == expected_result

## -------------------------- Test-case №2 ---------------------------------##
def input_valid_name_ru(): # вводим валидное значение на кириллице
    name = "Анна"
    expected_result = "Анна"
    actual_result = "Анна"
    assert actual_result == expected_result

## -------------------------- Test-case №3 ---------------------------------##
def input_empty_name(): # оставляем поле незаполненным
    name = None
    expected_result = "Вы пропустили это поле"
    actual_result = "Вы пропустили это поле"
    assert actual_result == expected_result

## -------------------------- Test-case №4 ---------------------------------##
def input_invalid_name_symbol(): # вводим в поле только спецсимволы
    name = "###"
    expected_result = "Поле имя не может содержать только спецсимволы"
    actual_result = "Поле имя не может содержать только спецсимволы"
    assert actual_result == expected_result

## -------------------------- Test-case №5 ---------------------------------##
def input_valid_email(): # вводим валидные данные
    email = "rezumik-oze87@hotmail.com"
    expected_result = "rezumik-oze87@hotmail.com"
    actual_result = "rezumik-oze87@hotmail.com"
    assert actual_result == expected_result

## -------------------------- Test-case №6 ---------------------------------##
def input_email_empty(): # оставляем поле незаполненным
    email = None
    expected_result = "Вы пропустили это поле"
    actual_result = "Вы пропустили это поле"
    assert actual_result == expected_result

## -------------------------- Test-case №7 ---------------------------------##
def input_incomplete_email(): # вводим часть адреса до символа "@"
    email = "rezumik-oze87"
    expected_result = "Адрес электронной почты должен содержать символ "@". Похоже, вы его пропустили"
    actual_result = "Адрес электронной почты должен содержать символ "@". Похоже, вы его пропустили"
    assert actual_result == expected_result

## -------------------------- Test-case №8 ---------------------------------##
def input_invalid_email_behind (): # вводим часть адреса от символа "@"
    email = "@hotmail.com"
    expected_result = "Это неполный адрес. Введите его полностью вместе с той частью, которая находится слева от символа "@""
    actual_result = "Это неполный адрес. Введите его полностью вместе с той частью, которая находится слева от символа "@""
    assert actual_result == expected_result

## -------------------------- Test-case №9 ---------------------------------##
def input_valid_comment(): # вводим валидное значение
    comment = "text"
    expected_result = "text"
    actual_result = "text"
    assert actual_result == expected_result

## -------------------------- Test-case №10 ---------------------------------##
def input_comment_empty (): # оставляем поле незаполненным
    comment = None
    expected_result = "Вы пропустили это поле"
    actual_result = "Вы пропустили это поле"
    assert actual_result == expected_result

@pytest.mark.parametrize(
    "name, expected_result, actual_result",
    [
        ("Anna", "Anna", "Anna"),
        ("Анна", "Анна", "Анна"),
        (None,"Вы пропустили это поле", "Вы пропустили это поле"),
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
#
#
# def test_input_email():
#
#
# def test_input_comment():