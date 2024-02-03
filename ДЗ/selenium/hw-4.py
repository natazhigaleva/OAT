import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.python.org/")
element = driver.find_element(By.NAME, "q")
element.click()
element.send_keys("common")
element.send_keys(Keys.ENTER)
driver.save_screenshot("screen_1.png")
time.sleep(1)
element = driver.find_element(By.NAME, "q")
element.clear()
element.send_keys("docs")
element.send_keys(Keys.ENTER)
driver.save_screenshot("screen_2.png")
time.sleep(1)
driver.back()
driver.save_screenshot("screen_3.png")
time.sleep(1)
current_url = driver.current_url
print(current_url)
driver.forward()
driver.save_screenshot("screen_4.png")
time.sleep(1)
driver.quit()
