import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get("https://pokewars.pl")
    print(driver.title)

    search = driver.find_element_by_name("login")
    search.send_keys("nikodem382")
    search = driver.find_element_by_name("pass")
    search.send_keys("Carpediem1229")
    search.send_keys(Keys.RETURN)
    time.sleep(random.randint(0, 2))

    # search = driver.find_element_by_class_name("close_btn")
    # link = driver.find_element_by_link_text("...")
    # link.click()

    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, ".."))
        )
    except:
        time.sleep(random.randint(3, 8))
        driver.quit()  # zamyka okno
