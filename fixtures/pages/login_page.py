from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage


class LoginPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.XPATH, "//li[@class='nav-item'][2]")
    pass
