import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Desired capabilities for Appium
MOBILE_CONFIG = {
    "remoteHost": os.getenv("REMOTE_HOST"),
    "remotePort": int(os.getenv("REMOTE_PORT"))
}

def get_mobile_config():
    """Return mobile config as a dictionary."""
    return MOBILE_CONFIG
