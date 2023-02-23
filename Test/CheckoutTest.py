from selenium import webdriver
from Pages.Login import Login
from Pages.Products import Products
from Pages.Checkout import Checkout
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_checkout():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login = Login(driver)
    product = Products(driver)
    checkout = Checkout(driver)

    # login
    login.enter_username()
    login.enter_password()
    login.click_login_button()

    # add to cart
    product.add_backpack_to_cart()
    time.sleep(5)
    product.add_bikelight_to_cart()
    time.sleep(5)
    product.add_boltTshirt_to_cart()
    time.sleep(5)

    # checkout
    checkout.click_cart_icon()
    time.sleep(10)
    checkout.click_checkout_button()
    time.sleep(10)
    checkout.enter_firstname()
    time.sleep(3)
    checkout.enter_lastname()
    time.sleep(3)
    checkout.enter_zipcode()
    time.sleep(3)
    checkout.click_continue()
    time.sleep(3)
    checkout.finish_checkout()
    time.sleep(3)

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='complete-header']"))
    )

    actual_message = success_message.text
    expected_message = 'THANK YOU FOR YOUR ORDER'
    assert actual_message == expected_message, f"Checkout unsuccessful"
    time.sleep(5)


test_checkout()
