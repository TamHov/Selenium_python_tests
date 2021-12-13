import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#this is a test
driver = webdriver.Chrome()
driver.get("https://courses.letskodeit.com/practice%E2%80%8B")
driver.maximize_window()
driver.find_element(By.XPATH, "//*[contains(text(), 'Switch To Alert Example')]/following::input[1]").send_keys("test")
time.sleep(3)
driver.find_element(By.XPATH, "//*[contains(text(), 'Switch To Alert Example')]/following::input[3]").click()
time.sleep(5)
alert_obj = driver.switch_to.alert
alert_obj.accept()
time.sleep(5)

driver.close()