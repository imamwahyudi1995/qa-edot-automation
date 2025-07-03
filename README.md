# UI Automation Testing Project (Web & Mobile)

This project contains a framework for UI automation testing on Web and Mobile (Android) platforms. The framework is built using Python with Pytest as the test runner, Selenium for browser interaction, and Appium for mobile device interaction.

## Table of Contents
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create a Virtual Environment](#2-create-a-virtual-environment)
  - [3. Install Python Dependencies](#3-install-python-dependencies)
  - [4. Appium & Android Emulator Setup](#4-appium--android-emulator-setup)
  - [5. Configure Environment Variables](#5-configure-environment-variables)
- [Running Tests](#running-tests)
  - [Running All Tests](#running-all-tests)
  - [Running Web Tests](#running-web-tests)
  - [Running Mobile Tests](#running-mobile-tests)
  - [Running with Markers](#running-with-markers)
- [Test Reporting](#test-reporting)
  - [Allure Report](#allure-report)
  - [HTML Report](#html-report)

## Key Features
- **Page Object Model (POM)**: Separates test logic from UI page implementation details for easier maintenance.
- **Data-Driven**: Uses external files (JSON) for test data, allowing for flexible scenarios.
- **Cross-Platform**: Supports testing on both Web (using Selenium) and Mobile (using Appium) platforms.
- **Centralized Configuration**: Settings for each platform (Web/Mobile) are managed in separate configuration files.
- **Advanced Reporting**: Generates detailed and interactive test reports using Allure and Pytest-HTML.
- **Dependency Management**: Uses `requirements.txt` to manage all required Python packages.

## Project Structure
```
qa-edot-automation/
├── mobile/                 # All Mobile testing related code
│   ├── config/             # Appium & device configuration
│   ├── locators/           # UI element locators for each page
│   ├── pages/              # Page Objects implementation
│   └── tests/              # Test scripts
├── web/                    # All Web testing related code
│   ├── config/             # Selenium & browser configuration
│   ├── locators/           # UI element locators
│   ├── pages/              # Page Objects implementation
│   └── tests/              # Test scripts
├── reports/                # Output directory for test reports
│   ├── allure/
│   └── html/
├── test_data/              # Data files for testing (e.g., JSON)
├── utils/                  # Utilities and helper functions
├── conftest.py             # Global Pytest fixtures & configuration
├── requirements.txt        # List of Python dependencies
└── README.md               # This file
```

## Prerequisites
Before you begin, ensure your machine has the following software installed:
1.  **Python** (version 3.10 or higher)
2.  **Node.js** and **npm** (to install Appium)
3.  **Java Development Kit (JDK)** (required by Appium)
4.  **Android Studio** (for the Android SDK and emulator management)
5.  **Appium Server**: `npm install -g appium`
6.  **Appium UIAutomator2 Driver**: `appium driver install uiautomator2`

## Recommended IDE

This project is developed and maintained using [PyCharm](https://www.jetbrains.com/pycharm/). While you can use any editor, using PyCharm is recommended for a better development experience.

- **Opening the project**: Simply open the project's root folder in PyCharm.
- **Virtual Environment**: PyCharm should automatically detect the virtual environment (`.venv`) if you've created it. If not, you can configure the project interpreter in `File > Settings > Project > Python Interpreter`.
- **Test Runner**: To run tests directly from the IDE, it's best to set the default test runner to Pytest. Go to `File > Settings > Tools > Python Integrated Tools` and select `Pytest` as the "Default test runner".

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <YOUR_REPOSITORY_URL>
cd qa-edot-automation
```

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to keep project dependencies isolated from your global Python installation.
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Python Dependencies
Install all required Python packages from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Appium & Android Emulator Setup
1.  Open **Android Studio**.
2.  Go to the **Virtual Device Manager** and create or start an Android Virtual Device (Emulator).
3.  Ensure your emulator's name matches the one in your configuration (`DEVICE_NAME` in `.env`).
4.  Run the Appium Server in a separate terminal:
    ```bash
    appium
    ```

### 5. Configure Environment Variables
Create a file named `.env` in the project's root directory. Copy the content below and adjust the values as needed. This file is used to store sensitive and environment-specific configurations.

```env
# Variables for Mobile Testing
PLATFORM_NAME="Android"
DEVICE_NAME="emulator-5554"
AUTOMATION_NAME="UiAutomator2"
APP_PATH="C:/Users/wahyu/Downloads/ework1.20.5.apk" # Replace with the absolute path to your APK file
APP_PACKAGE="id.edot.ework.debug"
APP_ACTIVITY="id.edot.ework.ui.activity.SplashScreenActivity"
NO_RESET=True
FULL_RESET=False
REMOTE_HOST="127.0.0.1"
REMOTE_PORT=4723

# Variables for Web Testing (Example)
BASE_URL="https://app-staging.edot.id/"
BROWSER="chrome"

# Credentials & Test Data
MOBILE_EMAIL="it.qa@edot.id"
MOBILE_PASSWORD="it.QA2025"
COMPANY_ID="default_company_id"
```

## Running Tests
Ensure the Appium server is running for mobile tests.

### Running All Tests
```bash
pytest
```

### Running Web Tests
```bash
pytest web/
```

### Running Mobile Tests
```bash
pytest mobile/
```

### Running with Markers
You can run specific test groups using markers defined in `pytest.ini`.
```bash
# Example: Run all login tests
pytest -m login

# Example: Run critical tests
pytest -m critical
```

## Test Reporting

### Allure Report
This report provides a rich, interactive visualization of the test results.
1.  Run tests with the Allure flag:
    ```bash
    pytest --alluredir=reports/allure
    ```
2.  Serve the report using the Allure command-line tool:
    ```bash
    allure serve reports/allure
    ```

### HTML Report
This report is a concise, single HTML file.
1.  Run tests with the pytest-html flag:
    ```bash
    pytest --html=reports/html/report.html --self-contained-html
    ```
2.  Open the `report.html` file in your browser.
