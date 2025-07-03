import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from mobile.config.mobile_config import get_mobile_config
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@pytest.fixture(scope="function")
def mobile_driver():
    """Initialize Appium driver for mobile automation."""
    # Get mobile configuration
    mobile_config = get_mobile_config()

    # Extract connection parameters
    remote_host = mobile_config.pop("remoteHost")
    remote_port = mobile_config.pop("remotePort")

    # Store test data separately from capabilities
    test_data = {
        "email": os.getenv("MOBILE_EMAIL"),
        "password": os.getenv("MOBILE_PASSWORD"),
        "company_id": os.getenv("COMPANY_ID")
    }

    # Define capabilities based on the successful Appium Inspector session log
    capabilities = {
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "emulator-5554",
        "appium:app": "C:/Users/wahyu/Downloads/ework1.20.5.apk",
        "appium:appPackage": "id.edot.ework.debug",
        "appium:appActivity": "id.edot.onboarding.OnBoardingActivity",
        "appium:noReset": True,
    }

    # Appium server URL (standard format for Appium 2.x)
    appium_server_url = f"http://{remote_host}:{remote_port}"

    # Initialize driver with exact same capabilities as Appium Inspector
    appium_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(command_executor=appium_server_url, options=appium_options)

    # Attach test data to driver for access in tests
    driver.test_data = test_data

    yield driver
    driver.quit()
