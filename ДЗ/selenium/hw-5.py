import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://calcus.ru/kalkulyator-ipoteki")
driver.execute_script("window.scrollTo(0, 150)")
cost = driver.find_element(By.NAME, "cost")
cost.click()
cost.send_keys("3500000")
start_sum: WebElement = driver.find_element(By.NAME, "start_sum")
start_sum.click()
start_sum.send_keys("1500000")
period = driver.find_element(By.NAME, "period")
period.click()
period.send_keys("10")
percent = driver.find_element(By.NAME, "percent")
percent.click()
percent.send_keys("42.86")
payment_type = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[10]/div[2]/label/span")
payment_type.click()
driver.save_screenshot("calculyator.png")
button_submit = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[12]/div/input")
button_submit.click()
time.sleep(3)
culc_result = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[16]")
driver.execute_script("arguments[0].scrollIntoView();", culc_result)
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-overlay']")))
time.sleep(5)
driver.save_screenshot("calc_result.png")
calc_result_table = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[1]/form/div[19]")
driver.execute_script("arguments[0].scrollIntoView();", calc_result_table)
wait = WebDriverWait(driver, timeout=10)
wait.until(EC.invisibility_of_element_located((By.XPATH, "//div[@class='loading-overlay']")))
time.sleep(5)
driver.save_screenshot("calc_result_table.png")
print("All elements was find!")
driver.quit()

