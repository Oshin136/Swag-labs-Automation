from seleniumpagefactory.Pagefactory import PageFactory


class Login(PageFactory):
    def __init__(self,driver):
        self.driver = driver

    locators = {
        'username':('id','user-name'),
        'password':('id','password'),
        'login_btn':('id','login-button')
    }

    def enter_username(self):
        self.username.send_keys('standard_user')

    def enter_password(self):
        self.password.send_keys('secret_sauce')

    def click_login_button(self):
        self.login_btn.click()