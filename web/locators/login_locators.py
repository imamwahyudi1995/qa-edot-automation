from selenium.webdriver.common.by import By

class LoginLocators:
    USE_EMAIL_LINK = (By.XPATH, "//button[normalize-space()='Use Email or Username']")
    EMAIL_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Log In']")
    ERROR_MESSAGE = (By.XPATH, "//*[normalize-space()='Incorrect password']")
    WELCOME_TEXT = (By.XPATH, "//span[normalize-space()='Welcome Back,']") 