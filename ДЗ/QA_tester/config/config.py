import pytest
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.get("https://webtucre.ru/testovaya-stranicza-4/")
    driver.maximize_window()
    yield driver

    driver.quit()
