from web.pages.base_page import BasePage
from web.locators.login_locators import LoginLocators
from web.config.web_config import get_web_config

class LoginPage(BasePage):
    def load(self):
        """Navigate to the login page URL from config."""
        config = get_web_config()
        self.driver.get(config["url"])

    def click_use_email(self):
        """Click the 'Use Email or Username' button to switch to email login form."""
        self.do_click(LoginLocators.USE_EMAIL_LINK)

    def enter_email(self, email):
        """Enter the email or username into the email input field."""
        self.do_send_keys(LoginLocators.EMAIL_INPUT, email)

    def enter_password(self, password):
        """Enter the password into the password input field."""
        self.do_send_keys(LoginLocators.PASSWORD_INPUT, password)

    def click_login(self):
        """Click the submit/login button."""
        self.do_click(LoginLocators.SUBMIT_BUTTON)

    def get_error_message(self):
        """Get the error message text displayed on failed login."""
        return self.get_text(LoginLocators.ERROR_MESSAGE)

    def is_welcome_text_visible(self):
        """Check if the welcome text is visible after successful login."""
        try:
            self.utils.wait_for_element_visible(LoginLocators.WELCOME_TEXT)
            return True
        except Exception:
            return False

    def is_error_message_visible(self):
        """Check if the error message is visible after failed login."""
        try:
            self.utils.wait_for_element_visible(LoginLocators.ERROR_MESSAGE)
            return True
        except Exception:
            return False

    def login(self, email, password):
        """Combined login step for legacy compatibility (not used in new flow)."""
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
