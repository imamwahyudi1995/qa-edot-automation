from utils.selenium_utils import SeleniumUtils

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.utils = SeleniumUtils(driver)

    def do_click(self, locator):
        """Wait for element to be clickable and then click."""
        self.utils.click(locator)

    def do_send_keys(self, locator, text):
        """Wait for element to be visible and send keys."""
        self.utils.send_keys(locator, text)

    def get_text(self, locator):
        """Wait for element to be visible and return its text."""
        element = self.utils.wait_for_element_visible(locator)
        return element.text

    def wait_for_element_visible(self, locator):
        """Wait until the element located by 'locator' is visible."""
        return self.utils.wait_for_element_visible(locator)
