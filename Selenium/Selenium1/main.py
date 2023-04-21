import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class Oak:
    def __init__(self):
        pass


class Elm:
    def __init__(self):
        pass

    def run(self):
        pass


class Schedule:

    def __init__(self):
        self.pokewars = "https://pokewars.pl"
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

    def login(self):
        self.driver.get(self.pokewars)
        search = self.driver.find_element(By.NAME, "login")
        search.send_keys("nikodem382")
        search = self.driver.find_element(By.NAME, "pass")
        search.send_keys("Carpediem1229")
        search.send_keys(Keys.RETURN)

    def run(self):
        self.login()
        poluj = self.driver.find_element(By.ID, "search_input")

        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    bot = Schedule()
    bot.run()

