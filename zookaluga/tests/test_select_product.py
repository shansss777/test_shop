import time

from selenium import webdriver

from base.base_class import Base
from pages.goods_page import Goods_page
from pages.start_page import Start_page


def test_select_cat_product(set_up, set_group):
    driver = webdriver.Chrome(executable_path='C:\\Users\\Onyx87\\PycharmProjects\\zookaluga\\chromedriver.exe')
    print("Start test 1")

    bc = Base(driver)
    bc.authorization()

    sp = Start_page(driver)
    sp.select_cat()

    gp = Goods_page(driver)
    gp.cat_goods()

    time.sleep(4)

    print("Finish Test")