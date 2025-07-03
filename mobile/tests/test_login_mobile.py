import pytest
from mobile.pages.login_screen import LoginScreen
from mobile.pages.dashboard_screen import DashboardScreen

@pytest.mark.usefixtures("mobile_driver")
def test_login_successful(mobile_driver):
    """Test successful login scenario."""
    login_screen = LoginScreen(mobile_driver)

    # Get credentials from driver test data
    email = mobile_driver.test_data["email"]
    password = mobile_driver.test_data["password"]
    company_id = mobile_driver.test_data["company_id"]

    # Complete login flow
    login_screen.enter_company_id(company_id)
    login_screen.enter_username(email)
    login_screen.enter_password(password)
    login_screen.click_login()

    # Verify login success
    dashboard_screen = DashboardScreen(mobile_driver)
    assert dashboard_screen.is_dashboard_visible(), "Dashboard should be visible after successful login."

@pytest.mark.usefixtures("mobile_driver")
def test_login_failed_invalid_credentials(mobile_driver):
    """Test failed login scenario with invalid credentials."""
    login_screen = LoginScreen(mobile_driver)

    # Get valid company_id but use invalid credentials
    company_id = mobile_driver.test_data["company_id"]

    login_screen.enter_company_id(company_id)
    login_screen.enter_username("invalid_user")
    login_screen.enter_password("invalid_password")
    login_screen.click_login()

    # Verify error message
    error_message = login_screen.get_error_message()
    assert "Invalid credentials" in error_message, f"Expected error message about invalid credentials, but got: {error_message}"
