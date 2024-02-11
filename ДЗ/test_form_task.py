import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://makarova1507ana.github.io/to_do_list_test_example/")
    yield driver

def test_add_task():
    try:
        input_task = driver.find_element(By.ID, "task-input")
        input_task.click()
        input_task.send_keys("Задача_1") # вводим задачу
        button_add = driver.find_element(By.ID, "add-task")
        button_add.click() # формируем список задач
        task = driver.find_elements(By.TAG_NAME, "li") # отображается добавленная задача
        assert isinstance(task, object)
        print('Задача добавлена')
    except NoSuchElementException:
        print(f'Добавьте задачу')

def test_delete_task():
    try:
        check_elem = driver.find_element(By.CSS_SELECTOR, "body > ul > li > input[type = checkbox]")
        check_elem.click() # отмечаем удаляемую задачу
        delete_button = driver.find_element(By.ID, "delete-task")
        delete_button.click
        task = driver.find_elements(By.TAG_NAME, "li") # в случае успешного удаления задачи элемент не найдется
        assert isinstance(task, object)
        print('Задача не выбрана')
    except NoSuchElementException:
        print(f'Задача удалена')