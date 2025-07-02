import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SeleniumUtils:
    _global_timeout = int(os.getenv("SELENIUM_TIMEOUT", 10))

    @classmethod
    def set_timeout(cls, timeout):
        """Set global timeout for all SeleniumUtils waits."""
        cls._global_timeout = timeout

    @classmethod
    def get_timeout(cls):
        return cls._global_timeout

    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout or SeleniumUtils._global_timeout

    def wait_for_element_visible(self, locator, timeout=None):
        """Wait until the element located by 'locator' is visible."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_clickable(self, locator, timeout=None):
        """Wait until the element located by 'locator' is clickable."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_contains(self, text, timeout=None):
        """Wait until the current URL contains the given text."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.url_contains(text)
        )

    def click(self, locator, timeout=None):
        """Wait for element to be clickable and then click."""
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def send_keys(self, locator, text, timeout=None):
        """Wait for element to be visible and send keys."""
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text) 