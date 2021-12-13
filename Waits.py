import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as W

driver = webdriver.Chrome()
URL = "https://www.wikipedia.org/"
driver.get(URL)
driver.maximize_window()

#driver.implicitly_wait(5)
#language_link = driver.find_element(By.XPATH, "//*[@id = 'js-link-box-en']")
language_link = W(driver, 5).until(EC.presence_of_element_located((By.XPATH, "//*[@id = 'js-link-box-en']")))
language_link.click()

search_box = driver.find_element(By.XPATH, "//*[@id = 'searchInput']")
search_box.send_keys("automation")
search_box.submit()
#time.sleep(5)
driver.back()

driver.close()