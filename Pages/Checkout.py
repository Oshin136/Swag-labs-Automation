from seleniumpagefactory.Pagefactory import PageFactory

class Checkout(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'cart_icon':('XPATH', "//a[@class='shopping_cart_link']"),
        'checkout_button':('id', 'checkout'),
        'checkout_firstname':('id','first-name'),
        'checkout_lastname':('id','last-name'),
        'checkout_zipcode':('id','postal-code'),
        'checkout_continue':('id','continue'),
        'checkout_finish':('id','finish')
    }

    def click_cart_icon(self):
        self.cart_icon.click()

    def click_checkout_button(self):
        self.checkout_button.click()

    def enter_firstname(self):
        self.checkout_firstname.send_keys("Oshin")

    def enter_lastname(self):
        self.checkout_lastname.send_keys("Gansi")

    def enter_zipcode(self):
        self.checkout_zipcode.send_keys('44800')

    def click_continue(self):
        self.checkout_continue.click()

    def finish_checkout(self):
        self.checkout_finish.click()


