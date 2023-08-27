from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):  # создаем переменные - элементы страницы
        self.driver = driver
        self.select_auth_by_mail = (By.ID, 't-btn-tab-mail')
        self.select_auth_by_phone = (By.ID, 't-btn-tab-phone')
        self.select_auth_by_login = (By.ID, 't-btn-tab-login')
        self.select_auth_by_ls = (By.ID, 't-btn-tab-ls')
        self.input_login = (By.ID, 'username')
        self.input_password = (By.ID, 'password')
        self.enter_bttn = (By.ID, 'kc-login')
        self.user_card = (By.XPATH, '//*[@class="base-card, home__info-card"]') #CssSelector - #app > main > div > div.home > div.base-card.home__info-card

    def load(self):
        self.driver.get('https://b2c.passport.rt.ru/')

        """проверяем загрузилась ли страница"""

    def is_loaded(self) -> bool:
        try:
            WDW(self.driver, timeout=5).until(EC.presence_of_element_located((self.select_auth_by_mail)))
            return True
        except:
            return False

    # def element(self, yahz):
    #     return self.driver.find_element(yahz)
    #
    # def auth_by_mail(self, login, password): # = auth_by_mail(self, login, query: str):
    #     self.element(*self.select_auth_by_mail).click()
    #     self.element(*self.input_login).send_keys(login)
    #     self.element(*self.input_password).send_keys(password)
    #     self.element(*self.enter_bttn).click()

    def auth_by_mail(self, login, password):
        self.driver.find_element(*self.select_auth_by_mail).click()
        self.driver.find_element(*self.input_login).send_keys(login)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.enter_bttn).clik()

    def auth_by_phone(self, login, password):
        self.driver.find_element(*self.select_auth_by_phone).click()
        self.driver.find_element(*self.input_login).send_keys(login)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.enter_bttn).clik()

    def auth_by_login(self, login, password):
        self.driver.find_element(*self.select_auth_by_login).click()
        self.driver.find_element(*self.input_login).send_keys(login)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.enter_bttn).clik()

    def auth_by_ls(self, login, password):
        self.driver.find_element(*self.select_auth_by_ls).click()
        self.driver.find_element(*self.input_login).send_keys(login)
        self.driver.find_element(*self.input_password).send_keys(password)
        self.driver.find_element(*self.enter_bttn).clik()

    # def search_for_product (self, query:str):
    #     search_input = self.driver.find_element(*self.check_box)
    #     search_input.send_keys(query)
    #     self.driver.find_element(*self.search_bttn).clik()

    def check_user_page_url(self) -> bool:
        try:
            WDW(self.driver, timeout=5).until(EC.presence_of_element_located((self.user_card)))
            if self.driver.current_url.startwith('https://b2c.passport.rt.ru/account_b2c/page?state=135354e7-1254-4122-8509-ac487bc8ce68&client_id=account_b2c#/'):
                return True
            return False
        except:
            return False

    def check_user_page_url_is_absent(self) -> bool:
        try:
            WDW(self.driver, timeout=5).until(EC.presence_of_element_located((self.user_card)))
            if self.driver.current_url.startwith('https://b2c.passport.rt.ru/account_b2c/page?state=135354e7-1254-4122-8509-ac487bc8ce68&client_id=account_b2c#/'):
                return False
            return True
        except:
            return True

