from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage
from models.register import RegisterUserModel


class RegistrationPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.XPATH, "//li[@class='nav-item'][2]")
    REGISTRATION_BUTTON_ON_LOGIN_PAGE = (By.CLASS_NAME, "btn-round")
    USERNAME_REG = (By.NAME, "username")
    FIRST_NAME_REG = (By.NAME, "first_name")
    PASS_1_REG = (By.NAME, "password1")
    PASS_2_REG = (By.NAME, "password2")
    EMAIL_REG = (By.NAME, "email")
    REG_BUTTON = (By.XPATH, "//input[@value='register']")
    TEXT_ON_HEAD_IN_LOG_IN_PAGE = (By.CLASS_NAME, "head")
    ERROR_TEXT = (By.XPATH, "//ul[@class='errorlist']/li")
    AGE = (By.NAME, "age")
    IMAGE_UPLOAD = (By.NAME, "avatar")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    LOGIN_BUTTON_ON_LOGIN_PAGE = (By.XPATH, "//input[@class='form-control'][@type='submit']")
    PROFILE_BUTTON = (By.CLASS_NAME, "dropdown-toggle")
    PROFILE_DROP_DOWN = (By.XPATH, "//a[@class='dropdown-item'][1]")
    PROFILE_IMAGE = (By.XPATH, "//p[5]")

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
        self.clear(locator=self.USERNAME_REG)
        self.fill(locator=self.USERNAME_REG, value=data.username)
        self.clear(locator=self.FIRST_NAME_REG)
        self.fill(locator=self.FIRST_NAME_REG, value=data.firstname)
        self.clear(locator=self.PASS_1_REG)
        self.fill(locator=self.PASS_1_REG, value=data.password_1)
        self.clear(locator=self.PASS_2_REG)
        self.fill(locator=self.PASS_2_REG, value=data.password_2)
        self.clear(locator=self.EMAIL_REG)
        self.fill(locator=self.EMAIL_REG, value=data.email)
        self.click_element(locator=self.REG_BUTTON)

    def text_on_head_in_log_in_page(self) -> str:
        """
        Element "Log in" on Head on "sign in" page.
        """
        element = self.text(locator=self.TEXT_ON_HEAD_IN_LOG_IN_PAGE)
        return element

    def text_error_reg_page(self) -> str:
        """
        Errors on reg page.
        """
        element = self.text(locator=self.ERROR_TEXT)
        return element

    def text_many_errors_reg_page(self) -> list:
        """
        All errors on reg page.
        """
        element = self.text_on_all_same_fields(locator=self.ERROR_TEXT)
        return element

    def clear_and_fill(self, data):
        """
        Element "Age" on reg page.
        """
        self.clear(locator=self.AGE)
        self.fill(locator=self.AGE, value=data)

    def avatar_upload(self, file_path):
        """
        Upload image on reg page.
        """
        self.upload_img(locator=self.IMAGE_UPLOAD, file_path=file_path)

    def login(self, username, password):
        """
        Upload image on reg page.
        """
        self.clear(locator=self.USERNAME_LOGIN)
        self.fill(locator=self.USERNAME_LOGIN, value=username)
        self.clear(locator=self.PASSWORD_LOGIN)
        self.fill(locator=self.PASSWORD_LOGIN, value=password)
        self.click_element(locator=self.LOGIN_BUTTON_ON_LOGIN_PAGE)

    def enter_on_profile_page(self):
        """
        Open profile menu.
        """
        self.click_element(locator=self.PROFILE_BUTTON)
        self.click_element(locator=self.PROFILE_DROP_DOWN)

    def profile_image_check(self) -> str:
        """
        Open profile menu.
        """
        element = self.text(locator=self.PROFILE_IMAGE)
        return element
