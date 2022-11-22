import datetime
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    url = 'https://www.zookaluga.ru/'

    # Locators
    come_in = "//a[@class='basket-line-block-icon-profile']"
    user_login = "//input[@name='USER_LOGIN']"
    user_password = "//input[@name='USER_PASSWORD']"
    enter_button = "//input[@name='Login']"

    def __init__(self, driver):
        self.driver = driver

    # Getters
    def get_come_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.come_in)))
    def get_user_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_login)))
    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_password)))

    def get_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.enter_button)))

    # Action
    def click_come_in(self):
        self.get_come_in().click()
        print("Click --Войти--")
    def input_user_login(self, login):
        self.get_user_login().send_keys(login)
        print("Input login")
    def input_user_password(self, password):
        self.get_user_password().send_keys(password)
        print("Input password")
    def click_enter_button(self):
        self.get_enter_button().click()
        print("Click --Enter button--")

    """Получаем current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Текущий URL : " + get_url)

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert price"""

    def assert_price(self, price_product, result):
        assert price_product == result
        print("Good value_price_product")

    """Method save screenshot"""

    def get_screenshot(self):

        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\Onyx87\\PycharmProjects\\zookaluga\\screen\\' + name_screenshot)

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_come_in()
        self.input_user_login("Likvidator")
        self.input_user_password("qwert123")
        self.click_enter_button()
