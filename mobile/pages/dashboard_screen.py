from appium.webdriver.common.appiumby import AppiumBy

class DashboardScreen:
    def __init__(self, driver):
        self.driver = driver

    def is_dashboard_visible(self):
        """Check if the dashboard is visible."""
        dashboard_locator = (AppiumBy.ID, "id.edot.ework.debug:id/rv_main_menu")
        return self.driver.find_element(*dashboard_locator).is_displayed()

    def navigate_to_customer_screen(self):
        """Navigate to the customer screen from the dashboard."""
        customer_screen_button_locator = (AppiumBy.ID, "id.edot.ework.debug:id/menu_customers")
        self.driver.find_element(*customer_screen_button_locator).click()
