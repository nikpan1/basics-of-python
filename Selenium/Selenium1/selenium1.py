import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://orteil.dashnet.org/cookieclicker")

    driver.implicitly_wait(5)

    cookie = driver.find_element_by_id("bigCookie")
    cookie_count = driver.find_element_by_id("cookies")

#    items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

    actions = ActionChains(driver)
    actions.click(cookie)

    for i in range(5000):
        actions.perform()

    driver.quit()
