import time
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, app):
        self.app = app

    def _find_element(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        element = WebDriverWait(self.app.driver, wait_time).until(
            expected_conditions.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return element

    def _find_all_elements(self, locator, wait_time=20):
        """
        Find element. Use Explicit wait
        :param locator: locator like (By.ID, 'name')
        :param wait_time: wait time
        :return: return selenium element
        """
        elements = WebDriverWait(self.app.driver, wait_time).until(
            expected_conditions.presence_of_all_elements_located(locator),
            message=f"Can't find element by locator {locator}",
        )
        return elements

    def click_element(self, locator, wait_time=20):
        """
        Click element.
        """
        element = self._find_element(locator, wait_time)
        element.click()

    def fill(self, locator, value: str, wait_time=20):
        """
        Fill element (fill == send_keys)
        """
        element = self._find_element(locator, wait_time)
        if value:
            element.send_keys(value)

    def text(self, locator, wait_time=20) -> str:
        """
        Get element text.
        """
        element = self._find_element(locator, wait_time)
        return element.text

    def open_page(self, url: str):
        """
        Open page.
        """
        self.app.driver.get(url)

    def clear(self, locator, wait_time=20):
        """
        Clear element.
        """
        element = self._find_element(locator, wait_time)
        element.clear()

    def re_fresh(self, locator, wait_time=20):
        """
        Refresh element.
        """
        element = self._find_element(locator, wait_time)
        element.send_keys(Keys.F5)

    def text_on_all_same_fields(self, locator, wait_time=10) -> list:
        """
        Get elementS text.
        """
        elements = self._find_all_elements(locator, wait_time)
        text_from_all_fields = []
        for i in elements:
            n = i.text
            text_from_all_fields.append(n)
        return text_from_all_fields

    def wait_element_text(self, locator, text, wait_time=5):
        """
        Реализация слипа через явные ожидания.
        """
        timestamp = time.time() + wait_time
        while time.time() < timestamp:
            element = self._find_element(locator)
            print(element.text, text)
            if element.text == text:
                return text
            time.sleep(0.5)
        raise Exception
