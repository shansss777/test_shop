import time

from selenium.webdriver import ActionChains

from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Goods_page(Base):



    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    left_slider = "//*[@id='left_slider_c4ca4238a0b923820dcc509a6f75849b']"
    right_slider = "//*[@id='right_slider_c4ca4238a0b923820dcc509a6f75849b']"
    manufacturer = "//*[@id='bx_eshop_wrap']/div[1]/div/div/div/div/div[1]/div[1]/div/div/form/div[1]/div[3]/div[1]/span[1]"
    brit = "//*[@id='arrFilter_134_710805328']"
    # gigvi = "//*[@id='bx_eshop_wrap']/div[1]/div/div/div/div/div[1]/div[1]/div/div/form/div[1]/div[3]/div[2]/div/div/div[26]/label"
    gigvi = "//input[@id='arrFilter_134_3395602792']"
    applay = "//input[@name='set_filter']"
    royal_canin = "//input[@id='arrFilter_134_2640904063']"
    select_poduct_1 = "//*[@id='bx_3966226736_34704_c80764dfaf26ca80162484593ec7c29b']/div/h3/a"
    select_poduct_2 = "//*[@id='bx_3966226736_34704_c80764dfaf26ca80162484593ec7c29b_pict_slider']/span[1]"
    cart = "//*[@id='bx_3966226736_34704_c80764dfaf26ca80162484593ec7c29b_buy_link']"
    go_to_cart = "//*[@id='CatalogSectionBasket_bx_3966226736_34704_c80764dfaf26ca80162484593ec7c29b']/div[3]/button"
    next_page = "Моя корзина"
    next_url = "https://www.zookaluga.ru/personal/cart/"
    cart_text = "//*[@id='pagetitle']"
    price_product_gp = "//*[@id='bx_3966226736_34704_c80764dfaf26ca80162484593ec7c29b_price']"
    price_product_cp = "//*[@id='basket-root']/div[1]/div/div/div[2]/div/div[2]/div/div"




    # Getters

    def get_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer)))

    def get_gigvi(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.gigvi)))

    def get_applay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.applay)))

    def get_brit(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brit)))

    def get_royal_canin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.royal_canin)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    def get_cart_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_text)))

    def get_price_product_gp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_gp)))

    def get_price_product_cp(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_cp)))

    # Actions

    def move_left_slider(self):
        action = ActionChains(self.driver)
        price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.left_slider)))
        action.click_and_hold(price).move_by_offset(100, 0).release().perform()
        print("GO left slider")

    def move_right_slider(self):
        action = ActionChains(self.driver)
        price = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.right_slider)))
        action.click_and_hold(price).move_by_offset(-80, 0).release().perform()
        print("GO right slider")

    def move_select_poduct(self):
        action = ActionChains(self.driver)
        add_select_poduct = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_poduct_2)))
        action.move_to_element(add_select_poduct).perform()
        print("Move to product")
        time.sleep(3)

    def click_manufacturer(self):
        self.get_manufacturer().click()
        print("Click manufacturer")

    def click_gigvi(self):
        self.get_gigvi().click()
        print("Select gigvi")

    def click_brit(self):
        self.get_brit().click()
        print("Select brit")

    def click_royal_canin(self):
        self.get_royal_canin().click()
        print("Select royal_canin")

    def click_applay(self):
        self.get_applay().click()
        print("Click applay")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart_button")

    def return_word(self, word):
        value_word = word.text
        print("Получаем значение : " + value_word)
        return value_word

    # Methods

    def cat_goods(self):
        self.get_current_url()
        self.move_left_slider()
        self.move_right_slider()
        self.click_manufacturer()
        self.click_gigvi()
        self.click_brit()
        self.click_royal_canin()
        time.sleep(1)
        self.click_applay()
        self.price_1 = self.return_word(self.get_price_product_gp())
        print(self.price_1)
        self.move_select_poduct()
        self.click_cart()
        self.click_cart_button()
        self.assert_word(self.get_cart_text(), self.next_page)
        self.assert_url(self.next_url)
        self.assert_price(self.price_1, self.return_word(self.get_price_product_cp()))
        time.sleep(20)
