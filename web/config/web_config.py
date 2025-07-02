import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

WEB_URL = os.getenv("WEB_URL")
WEB_EMAIL = os.getenv("WEB_EMAIL")
WEB_PASSWORD = os.getenv("WEB_PASSWORD")

def get_web_config():
    """Return web config as a dictionary."""
    return {
        "url": WEB_URL,
        "email": WEB_EMAIL,
        "password": WEB_PASSWORD
    }
