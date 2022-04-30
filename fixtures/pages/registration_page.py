from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel


class RegistrationPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.XPATH, "//li[@class='nav-item'][2]")
    REGISTRATION_BUTTON_ON_LOGIN_PAGE = (By.CLASS_NAME, "btn-round")
    USERNAME = (By.NAME, "username")
    FIRST_NAME = (By.NAME, "first_name")
    PASS_1 = (By.NAME, "password1")
    PASS_2 = (By.NAME, "password2")
    EMAIL = (By.NAME, "email")
    REG_BUTTON = (By.XPATH, "//input[@value='register']")
    TEXT_ON_HEAD_IN_LOG_IN_PAGE = (By.CLASS_NAME, "head")
    ALREADY_EXISTS = (By.XPATH, "//ul[@class='errorlist']/li")

    # def reg_interface_image(self):
    #     element = self.app.driver.find_element(*self.REG_INTERFACE_IMAGE)
    #     element = self.app.driver.find_element(*self.REG_INTERFACE_REG_NEW_USER)

    def open_registration_page(self):
        """
        Open login page.
        """
        self.open_page(self.app.url)
        self.click_element(locator=self.LOGIN_BUTTON_ON_HEADER)
        self.click_element(locator=self.REGISTRATION_BUTTON_ON_LOGIN_PAGE)

    def entry_data_registration(self, data: RegisterUserModel):
        """
        Data entry in fields.
        """
        self.clear(locator=self.USERNAME)
        self.fill(locator=self.USERNAME, value=data.username)
        self.clear(locator=self.FIRST_NAME)
        self.fill(locator=self.FIRST_NAME, value=data.firstname)
        self.clear(locator=self.PASS_1)
        self.fill(locator=self.PASS_1, value=data.password_1)
        self.clear(locator=self.PASS_2)
        self.fill(locator=self.PASS_2, value=data.password_2)
        self.clear(locator=self.EMAIL)
        self.fill(locator=self.EMAIL, value=data.email)
        self.click_element(locator=self.REG_BUTTON)

    def text_on_head_in_log_in_page(self) -> str:
        """
        Element "Log in" on Head on "sign in" page.
        """
        element = self.text(locator=self.TEXT_ON_HEAD_IN_LOG_IN_PAGE)
        return element

    def text_username_already_exists(self) -> str:
        """
        Element "Log in" on Head on "sign in" page.
        """
        element = self.text(locator=self.ALREADY_EXISTS)
        return element

    # def reg_status_big_red_tab(self) -> str:
    #     """
    #     алертная всплывашка снизу на невалидные данные.
    #     """
    #     element = self.text(locator=self.MESSAGE_REG_STATUS_ERROR_BIG_RED)
    #     return element
    #
    # def all_toast_statuses(self) -> list:
    #     """информационная всплывашка справа-вверху"""
    #     element = self.text_on_all_same_fields(locator=self.MESSAGE_REG_STATUS_TOP_RIGHT)
    #     return element
