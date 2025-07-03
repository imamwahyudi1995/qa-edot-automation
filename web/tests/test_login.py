import pytest
from web.pages.login_page import LoginPage
from web.config.web_config import get_web_config

@pytest.mark.usefixtures("driver")
def test_login_successful(driver):
    """
    Test successful login scenario:
    1. Click 'Use Email or Username' button
    2. Enter valid email
    3. Click submit
    4. Enter valid password
    5. Click submit
    6. Assert that the welcome text is visible (login success)
    """
    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password(config["password"])
    login_page.click_login()
    assert login_page.is_welcome_text_visible(), "Welcome text should be visible after successful login."

@pytest.mark.usefixtures("driver")
def test_login_failed_invalid_password(driver):
    """
    Test failed login scenario with invalid password:
    1. Click 'Use Email or Username' button
    2. Enter valid email
    3. Click submit
    4. Enter invalid password
    5. Click submit
    6. Assert that the error message is visible (login failed)
    """
    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password("password123")
    login_page.click_login()
    assert login_page.is_error_message_visible(), "Error message should be visible for invalid login."