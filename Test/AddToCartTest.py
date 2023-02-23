from selenium import webdriver
from Pages.Login import Login
from Pages.Products import Products
import time


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login = Login(driver)
    product = Products(driver)

    login.enter_username()
    login.enter_password()
    login.click_login_button()

    product.add_backpack_to_cart()
    time.sleep(5)
    product.add_bikelight_to_cart()
    time.sleep(5)
    product.add_boltTshirt_to_cart()

    time.sleep(10)


test_add_to_cart()
