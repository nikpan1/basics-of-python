import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

LOGIN = "nikodem382"
PASSWORD = "Carpediem1229"
# to jest do zmiany


def search_in_text(word, long):
    for i in range(0, len(long)):
        if long[i] == word[0]:
            if word == long[i:(i + len(word))]:
                return True
    return False


def user_reaction():
    print("Czekam na użytkownika. [PRESS ANY KEY]")
    a = input()


# a, b - in seconds
def wait(a, b):
    t = random.uniform(a * 100, b * 100)
    t = t / 100
    time.sleep(t)


def random_wait():
    if random.randint(1, 13) in [1, 2, 3]:
        wait(0, random.randint(1, 4) + 1)


class Elm:
    def __init__(self):
        pass


class Samson:
    def __init__(self, driver):
        self.driver = driver


# Throw poke ball
class Throw:
    def __init__(self, driver):
        self.driver = driver

    def netball(self):
        try:
            cth = self.driver.find_element(By.XPATH, "//form[@name='pokeball_Netball']")
            cth.click()
        except:
            return True

    def levelball(self):
        try:
            cth = self.driver.find_element(By.XPATH, "//form[@name='pokeball_Levelball']")
            cth.click()
        except:
            return True

    def ultraball(self):
        try:
            cth = self.driver.find_element(By.XPATH, "//form[@name='pokeball_Ultraball']")
            cth.click()
        except:
            return True

    def repeatball(self):
        try:
            cth = self.driver.find_element(By.XPATH, "//form[@name='pokeball_Repeatball']")
            cth.click()
        except:
            print("Błąd nie mogę użyć netballa!")
            user_reaction()
            return True


class Statements:
    def __init__(self, driver):
        self.driver = driver

    def is_full(self):
        search = self.driver.find_element(By.CLASS_NAME, "rezerwa_info")
        st = search.text.split(" ")

        if int(st[1]) > 28:
            print("Rezerwa jest pełna!")
            return True
        return False

    # mozna przemyslec to - w sumie mozna to o wiele lepiej zrobic
    def is_end_pa(self):
        search = self.driver.find_element(By.XPATH, "//span[@id='action_points_count']")
        if int(search.text) < 5:
            print("PA się skończyło!")
            return True
        else:
            return False

    def have_item(self):
        try:
            search = self.driver.find_element(By.XPATH, "//input[@name='zdejmij_przedmioty']")
            search.click()
            print("I took the item!")
        except:
            pass

    def is_pokemon(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            if search_in_text("dzikiego", search.text):
                sr = search.text.split(" ")
                print(sr[-1])
            return search_in_text("dzikiego", search.text)
        except:
            return False

    def is_shiny(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            return search_in_text("Shiny", search.text)
        except:
            return False

    def is_trainer(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            return search_in_text("drodze trenera", search.text)
        except:
            return False

    def is_empty(self):
        search = self.driver.find_element(By.XPATH, "//div[@class='alert-box error']")
        return search_in_text("nic ciekawego", search.text)

    def is_egg(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            print(search.text)
            return search_in_text("Inkubatora Regionu", search.text)
        except:
            return False

    def is_pole_magne(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            return search_in_text("etyczne", search.text)
        except:
            return False

    def is_porosnieta_ska(self):
        try:
            search = self.driver.find_element(By.XPATH, "//div[@class='alert-box info']")
            return search_in_text("poczu", search.text)
        except:
            return False

    def is_healthy(self):
        pass


class Schedule:
    def __init__(self):
        self.pokewars = "https://pokewars.pl"
        PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(PATH)

        self.pb = Throw(self.driver)
        self.st = Statements(self.driver)

    def login(self):
        search = self.driver.find_element(By.NAME, "login")
        search.send_keys(LOGIN)
        search = self.driver.find_element(By.NAME, "pass")
        search.send_keys(PASSWORD)
        search.send_keys(Keys.RETURN)
        # do zmiany

    def heal_all(self):
        try:
            search = self.driver.find_element(By.XPATH, "//img[@title='Wylecz wszystkie Pokemony']")
            search.click()
            try:
                search = self.driver.find_element(By.XPATH,
                                                  "//button[@class='vex-dialog-button-primary vex-dialog-button vex-first']")
                search.click()
            except:
                print("Nie mogłem nadusić ok po nieudanym uleczeniu...")
        except:
            print("próbowałem wyleczyć ale coś poszło nie tak")

    def sell_rezerwa(self):
        try:
            search = self.driver.find_element(By.XPATH, "//input[@title='Sprzedaj wszystkie pokemony']")
            search.click()
            try:
                wait(0, 1)
                search = self.driver.find_element(By.XPATH, "//button[@type='submit']")
                search.click()
            except:
                print("Nie mogłem nadusić ok po naduszeniu sell all...")

        except:
            print("próbowałem sprzedać rezerwę ale coś poszło nie tak")
        wait(0, 1)

    def drink_oak(self):
        search = self.driver.find_element(By.XPATH, "//img[@title='Wypij Napój Profesora Oaka']")
        search.click()
        wait(0, 0.5)

    def fight_pokemon(self):
        wait(0, 0.6)
        cth = self.driver.find_element(By.XPATH, "//form[@name='poke_53785589']")
        try:
            cth.click()
        except:
            print("fight_pokemon() nie zadziałało.")
            user_reaction()
            cth.click()

        wait(0.1, 0.3)
        cth = self.driver.find_element(By.XPATH, "//a[@href='#wynik_walki']")
        cth.click()

    def catch_pokemon(self):
        # netball + levelball
        wait(0.1, 0.6)
        if self.pb.netball():
            pass
            print("Coś stało się nie git. (catch_pokemon, netball")
            user_reaction()

        wait(0, 0.4)
        if self.pb.levelball():
            pass
            # ?

    def catch_shiny(self):
        wait(0.1, 0.55)
        if self.pb.netball():
            print("Coś stało się nie git. (catch_shiny, netball)")
            user_reaction()

        # repeatball
        not_catched = True
        while not_catched:
            if self.pb.repeatball():
                not_catched = False

    def hunt(self):
        # JAKA LOKALIZACJA
        try:
            poluj = self.driver.find_element(By.XPATH, "//img[@src='img/lokacje/s/Squallville.jpg']")
            poluj.click()
        except:
            print("Coś uniemożliwia dalsze polowanie. [hunt()]")

    def make_screenshot(self):
        pass

    def run(self):
        self.driver.get(self.pokewars)
        self.login()

        catching = True  # kiedy zatrzymać
        skip = True
        while catching:
            if self.st.is_full():
                user_reaction()     # zautomatyzować - użytkownik wybiera czy program ma czekać w tych momentach
                self.sell_rezerwa()

            random_wait()
            self.hunt()

            if not skip:
                skip = True
                try:
                    search = self.driver.find_element(By.XPATH,
                                                      "//button[@class='vex-dialog-button-primary vex-dialog-button vex-first']")
                    search.click()
                except:
                    print("Coś jest nie tak. [jajko]")
                    user_reaction()
            if self.st.is_porosnieta_ska():
                print("Porośnięta skała!")
                user_reaction()
            if self.st.is_pole_magne():
                print("Pole magnetyczne!")
                user_reaction()
            if self.st.is_pokemon():
                if self.st.is_shiny():
                    print("____________________")
                    for i in range(3):
                        print("UWAGA, SHINY.")
                    print("____________________")
                    user_reaction()
                    # self.make_screenshot()
                    # self.fight_pokemon()
                    # self.catch_shiny()
                else:
                    self.fight_pokemon()
                    self.catch_pokemon()

                self.st.have_item()

            elif self.st.is_trainer():
                print("Lecze pokemony!")
                self.heal_all()
            elif self.st.is_egg():
                skip = False
            else:
                pass

            if self.st.is_end_pa():
                print("Pije Oaka!")
                self.drink_oak()

        self.driver.close()


if __name__ == "__main__":
    option = webdriver.ChromeOptions()
    option.add_argument('--disable-blink-features=AutomationControlled')

    bot = Schedule()
    bot.run()

# co jeżeli pokemon mi padł
# Spotkałeś nauczyciela ataków, który proponuje Ci naukę unikalnego ruchu dla jednego z Twoich Pokemonów. Oczywiście za drobną opłatą...
# File "C:\Users\Nikodem\PycharmProjects\pythonProject\main.py", line 238, in <module> File "C:\Users\Nikodem\PycharmProjects\pythonProject\main.py", line 199, in run try:
# pełna rezerwa x2
