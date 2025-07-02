import os
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="function")  # Use function scope for full test isolation and parallel execution
def driver():
    """
    Selenium WebDriver fixture configurable via .env:
    - SELENIUM_HEADLESS: true/false
    - SELENIUM_WINDOW_SIZE: width,height (e.g. 1280,1024)
    - SELENIUM_MAXIMIZE: true/false
    - SELENIUM_TIMEOUT: global implicit wait (seconds)
    - SELENIUM_BROWSER: chrome (default, can be extended)
    Each test gets a fresh browser instance for isolation and parallel safety.
    """
    headless = os.getenv("SELENIUM_HEADLESS", "true").lower() == "true"
    window_size = os.getenv("SELENIUM_WINDOW_SIZE", "1280,1024")
    maximize = os.getenv("SELENIUM_MAXIMIZE", "false").lower() == "true"
    timeout = int(os.getenv("SELENIUM_TIMEOUT", 10))
    browser = os.getenv("SELENIUM_BROWSER", "chrome").lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless')
        if window_size:
            options.add_argument(f'--window-size={window_size}')
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    else:
        raise NotImplementedError(f"Browser '{browser}' is not supported yet.")

    driver.implicitly_wait(timeout)
    if maximize:
        driver.maximize_window()
    yield driver
    driver.quit()
