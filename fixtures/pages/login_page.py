from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.XPATH, "//li[@class='nav-item'][2]")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    LOGIN_BUTTON_ON_LOGIN_PAGE = (By.XPATH, "//input[@class='form-control'][@type='submit']")
    SEE_ACCOMMODATION_MAIN_PAGE = (By.CLASS_NAME, "btn-danger")
    TEXT_ON_HEAD_IN_LOG_IN_PAGE = (By.CLASS_NAME, "head")
    ERROR_TEXT = (By.XPATH, "//ul[@class='errorlist nonfield']/li")
    PROFILE_BUTTON_ON_HEADER = (By.CLASS_NAME, "dropdown-toggle")

    def open_login_page(self):
        """
        Open login page.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.LOGIN_BUTTON_ON_HEADER)

    def login(self, username, password):
        """
        Upload image on reg page.
        """
        self.clear(locator=self.USERNAME_LOGIN)
        self.fill(locator=self.USERNAME_LOGIN, value=username)
        self.clear(locator=self.PASSWORD_LOGIN)
        self.fill(locator=self.PASSWORD_LOGIN, value=password)
        self.click_element(locator=self.LOGIN_BUTTON_ON_LOGIN_PAGE)

    def see_accommodation_main_page(self) -> str:
        """
        Element "See Accommodation" on Main page.
        """
        element = self.text(locator=self.SEE_ACCOMMODATION_MAIN_PAGE)
        return element

    def text_on_head_in_log_in_page(self) -> str:
        """
        Element "Log in" on Head on "Log in" page.
        """
        element = self.text(locator=self.TEXT_ON_HEAD_IN_LOG_IN_PAGE)
        return element

    def text_many_errors_login_page(self) -> list:
        """
        All errors on login page.
        """
        element = self.text_on_all_same_fields(locator=self.ERROR_TEXT)
        return element
