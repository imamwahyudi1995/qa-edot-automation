from mobile.locators.login_locators import LoginLocators

class LoginScreen:
    def __init__(self, driver):
        self.driver = driver
        self.locators = LoginLocators

    def enter_username(self, username):
        """Enter username into the username input field."""
        self.driver.find_element(*self.locators.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        """Enter password into the password input field."""
        self.driver.find_element(*self.locators.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        """Click the login button."""
        self.driver.find_element(*self.locators.LOGIN_BUTTON).click()

    def get_error_message(self):
        """Get the error message text displayed on failed login."""
        return self.driver.find_element(*self.locators.ERROR_MESSAGE).text

    def enter_company_id(self, company_id):
        """Enter company ID into the company ID input field."""
        self.driver.find_element(*self.locators.COMPANY_ID_INPUT).send_keys(company_id)
