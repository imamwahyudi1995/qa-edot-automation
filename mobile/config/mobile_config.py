import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Desired capabilities for Appium
MOBILE_CONFIG = {
    "platformName": os.getenv("PLATFORM_NAME", "Android"),
    "deviceName": os.getenv("DEVICE_NAME", "emulator-5554"),
    "app": os.getenv("APP_PATH", "path/to/your/app.apk"),
    "automationName": os.getenv("AUTOMATION_NAME", "UiAutomator2"),
    "noReset": os.getenv("NO_RESET", "true"),
    "fullReset": os.getenv("FULL_RESET", "false"),
}

def get_mobile_config():
    """Return mobile config as a dictionary."""
    return MOBILE_CONFIG

