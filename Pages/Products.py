from seleniumpagefactory.Pagefactory import  PageFactory

class Products(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'backpack_addtocart':('id','add-to-cart-sauce-labs-backpack'),
        'bikelight_addtocart':('id','add-to-cart-sauce-labs-bike-light'),
        'boltTshirt_addtocart':('id','add-to-cart-sauce-labs-bolt-t-shirt')
    }

    def add_backpack_to_cart(self):
        self.backpack_addtocart.click()

    def add_bikelight_to_cart(self):
        self.bikelight_addtocart.click()

    def add_boltTshirt_to_cart(self):
        self.boltTshirt_addtocart.click()