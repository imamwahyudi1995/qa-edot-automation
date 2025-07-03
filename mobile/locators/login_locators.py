from appium.webdriver.common.appiumby import AppiumBy

class LoginLocators:
    USERNAME_INPUT = (AppiumBy.ID, "id.edot.ework.debug:id/tv_username")
    PASSWORD_INPUT = (AppiumBy.ID, "id.edot.ework.debug:id/tv_password")
    LOGIN_BUTTON = (AppiumBy.ID, "id.edot.ework.debug:id/button_text")
    ERROR_MESSAGE = (AppiumBy.ID, "id.edot.ework.debug:id/tv_error_message")
    COMPANY_ID_INPUT = (AppiumBy.ID, "id.edot.ework.debug:id/tv_company_id")
