import pytest
from faker import Faker
from web.pages.login_page import LoginPage
from web.pages.company_page import CompanyPage
from web.config.web_config import get_web_config

@pytest.mark.usefixtures("driver")
def test_create_and_verify_company(driver):
    """
    Test case for creating a new company and verifying its details.
    1. Login to the application.
    2. Navigate to the Companies page.
    3. Create a new company using dummy data.
    4. Verify the company details on the detail page.
    """
    # Arrange: Login and prepare test data
    config = get_web_config()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.click_use_email()
    login_page.enter_email(config["email"])
    login_page.click_login()
    login_page.enter_password(config["password"])
    login_page.click_login()

    fake = Faker()
    company_data = {
        "name": fake.company(),
        "email": fake.email(),
        "phone": fake.msisdn(),
        "address": fake.address()
    }
    company_page = CompanyPage(driver)

    # Act: Create a new company and navigate to its detail page
    company_page.go_to_companies_page()
    company_page.create_company(company_data)
    company_page.manage_newly_created_company(company_data["name"])

    # Assert: Verify company name on detail page
    detail_company_name = company_page.get_company_name_from_detail_page(company_data["name"])
    assert detail_company_name == company_data["name"], f"Expected company name '{company_data['name']}', but got '{detail_company_name}'"

    # Assert: Verify company data on detail page
    company_page.verify_company_data_on_detail_page(company_data)
