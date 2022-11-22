from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Start_page(Base):

    #url = 'https://www.zookaluga.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators


    for_cat = "//a[@class='catalog-section-list-item-link']"
    cat_text = "//h1[@id='pagetitle']"



    # Getters

    def get_for_cat(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.for_cat)))
    def get_cat_text(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cat_text)))


    # Actions

    def click_for_cat(self):
        self.get_for_cat().click()
        print("Click Для кошек")

    # Methods

    def select_cat(self):
        self.get_current_url()
        self.click_for_cat()
        self.assert_word(self.get_cat_text(), 'Товары и корма для кошек')
        self.assert_url("https://www.zookaluga.ru/catalog/koshki/")