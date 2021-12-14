import time

from selenium import webdriver
from selenium.webdriver.common.by import By

#Added a comment
driver = webdriver.Chrome()
driver.get("https://courses.letskodeit.com/practice%E2%80%8B")
driver.maximize_window()
driver.switch_to.frame("iframe-name")
driver.find_element(By.XPATH, "//*[contains(text(), 'Complete Test Automation Bundle')]").click()
time.sleep(5)

driver.close()