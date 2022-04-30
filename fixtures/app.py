from fixtures.pages.registration_page import RegistrationPage
from fixtures.pages.order_page import OrderPage
from fixtures.pages.login_page import LoginPage


class Application:

    def __init__(self, driver, url: str):
        self.driver = driver
        self.url = url
        self.registration_page = RegistrationPage(self)
        self.login_page = LoginPage(self)
        self.order_page = OrderPage(self)

    def quit(self):
        self.driver.quit()
