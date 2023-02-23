from selenium import webdriver
from Pages.Login import Login
import time


def test_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login = Login(driver)

    login.enter_username()
    login.enter_password()
    login.click_login_button()

    time.sleep(5)


test_login()
