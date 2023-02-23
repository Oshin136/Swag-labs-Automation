from selenium import webdriver
from Pages.Login import Login

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

login = Login(driver)
test
