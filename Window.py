import time
from selenium import webdriver

driver = webdriver.Chrome()
URL = "https://www.wikipedia.org/"
languages = ["en", "fr", "ru"]

try:
    driver.get(URL)
    driver.maximize_window()
    print("current window handle: ", driver.current_window_handle)
    driver.implicitly_wait(5)

    for i in range(len(languages)):
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[i+1])
        language_url = "https://" + languages[i] + ".wikipedia.org/"
        driver.get(language_url)
        print(language_url, driver.current_window_handle, driver.title)
except:
    print("Something wrong happened")

finally:
    driver.quit()
