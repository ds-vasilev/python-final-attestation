from selenium.webdriver.common.by import By
from fixtures.pages.base_page import BasePage


class OrderPage(BasePage):
    LOGIN_BUTTON_ON_HEADER = (By.XPATH, "//li[@class='nav-item'][2]")
    USERNAME_LOGIN = (By.NAME, "username")
    PASSWORD_LOGIN = (By.NAME, "password")
    LOGIN_BUTTON_ON_LOGIN_PAGE = (By.XPATH, "//input[@class='form-control'][@type='submit']")
    BUTTON = (By.CLASS_NAME, "btn-danger")
    FIRST_CARD_ON_LIST_OF_ACCOMMODATION = (By.CLASS_NAME, "card")
    ACCOMMODATION_DETAILS = (By.CLASS_NAME, "ml-3")
    PROFILE_BUTTON_ON_HEADER = (By.CLASS_NAME, "dropdown-toggle")
    PROFILE_DROP_DOWN = (By.XPATH, "//a[@class='dropdown-item'][2]")
    BASKETS_HEADER = (By.CLASS_NAME, "head")
    BUTTON_ORDER_TO_THE_DESIGN = (By.CLASS_NAME, "btn-outline-success")
    ORDER_CREATE_HEADER = (By.CLASS_NAME, "h2")
    ORDER_SAVE = (By.XPATH, "//button[@type='submit']")
    YOUR_ORDER = (By.CLASS_NAME, "head")

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

    def button_click(self):
        """
        Booking first hotel.
        """
        self.click_element(locator=self.BUTTON)

    def element_first_card_on_list_of_accommodation(self) -> str:
        """
        Element_first_card_on_list_of_accommodation.
        """
        element = self.text(locator=self.FIRST_CARD_ON_LIST_OF_ACCOMMODATION)
        return element

    def element_accommodation_details(self) -> str:
        """
        Element_first_card_on_list_of_accommodation.
        """
        element = self.text(locator=self.ACCOMMODATION_DETAILS)
        return element

    def enter_on_basket_page(self):
        """
        Open profile menu.
        """
        self.click_element(locator=self.PROFILE_BUTTON_ON_HEADER)
        self.click_element(locator=self.PROFILE_DROP_DOWN)

    def text_on_baskets_header(self):
        """
        Text on baskets header.
        """
        element = self.text(locator=self.BASKETS_HEADER)
        return element

    def enter_in_order_to_the_design(self):
        """
        Enter in order.
        """
        self.click_element(locator=self.BUTTON_ORDER_TO_THE_DESIGN)

    def text_on_order_create(self):
        """
        Text on baskets header.
        """
        element = self.text(locator=self.ORDER_CREATE_HEADER)
        return element

    def order_save(self):
        """
        Order save
        """
        self.click_element(locator=self.ORDER_SAVE)

    def text_on_your_order(self):
        """
        Text on baskets header.
        """
        element = self.text(locator=self.YOUR_ORDER)
        return element
