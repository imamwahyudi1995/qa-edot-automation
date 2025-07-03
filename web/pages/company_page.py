from .base_page import BasePage
from ..locators.company_locators import CompanyLocators
import json
from pathlib import Path
from selenium.webdriver.common.by import By

class CompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CompanyLocators()
        self.company_data_path = Path("test_data/company_data.json")

    def load_company_data(self):
        """Load company data from JSON file."""
        with open(self.company_data_path, "r") as file:
            return json.load(file)

    def go_to_companies_page(self):
        self.wait_for_element_visible(self.locators.SETTING_NAV_LINK)
        try:
            self.do_click(self.locators.COMPANIES_NAV_LINK)
        except Exception:
            self.driver.refresh()
            self.do_click(self.locators.COMPANIES_NAV_LINK)

    def click_add_company(self):
        self.do_click(self.locators.ADD_COMPANY_BUTTON)

    def fill_registration_form1(self, company_data):
        self.do_send_keys(self.locators.COMPANY_NAME_INPUT, company_data["name"])
        self.do_send_keys(self.locators.EMAIL_INPUT, company_data["email"])
        self.do_send_keys(self.locators.PHONE_INPUT, company_data["phone"])
        self.do_send_keys(self.locators.STREET_ADDRESS_INPUT, company_data["address"])

        self.do_click(self.locators.INDUSTRY_TYPE_DROPDOWN)
        try:
            self.do_click(self.locators.INDUSTRY_OPTION)
        except Exception:
            self.do_click(self.locators.INDUSTRY_TYPE_DROPDOWN)
            self.do_click(self.locators.INDUSTRY_OPTION)

        self.do_click(self.locators.COMPANY_TYPE_DROPDOWN)
        try:
            self.do_click(self.locators.COMPANY_TYPE_OPTION)
        except Exception:
            self.do_click(self.locators.COMPANY_TYPE_DROPDOWN)
            self.do_click(self.locators.COMPANY_TYPE_OPTION)

        self.do_click(self.locators.LANGUAGE_TYPE_DROPDOWN)
        try:
            self.do_click(self.locators.LANGUAGE_OPTION)
        except Exception:
            self.do_click(self.locators.LANGUAGE_TYPE_DROPDOWN)
            self.do_click(self.locators.LANGUAGE_OPTION)

        self.do_click(self.locators.COUNTRY_TYPE_DROPDOWN)
        try:
            self.do_click(self.locators.COUNTRY_OPTION)
        except Exception:
            self.do_click(self.locators.COUNTRY_TYPE_DROPDOWN)
            self.do_click(self.locators.COUNTRY_OPTION)

        self.do_click(self.locators.PROVINCE_TYPE_DROPDOWN)
        self.do_click(self.locators.PROVINCE_OPTION)

        self.do_click(self.locators.CITY_TYPE_DROPDOWN)
        self.do_click(self.locators.CITY_OPTION)

        self.do_click(self.locators.DISTRICT_TYPE_DROPDOWN)
        self.do_click(self.locators.DISTRICT_OPTION)

        self.do_click(self.locators.SUB_DISTRICT_TYPE_DROPDOWN)
        # Check if the locator is visible and has less than 1 element
        list_combobox_locator = (By.XPATH, "//div[@id='list-combobox']//div/div")
        while len(self.driver.find_elements(*list_combobox_locator)) < 2:
            self.wait_for_element_visible(list_combobox_locator)

        self.do_click(self.locators.SUB_DISTRICT_OPTION)

        self.do_click(self.locators.NEXT_BUTTON)

    def fill_registration_form2(self):
        self.wait_for_element_visible(self.locators.FORM_STEP_2)
        self.do_click(self.locators.NEXT_BUTTON)

    def fill_registration_form3(self, company_data):

        branch_name_locator = (By.XPATH, "//input[@placeholder='Input Branch Name']")
        self.wait_for_element_visible(branch_name_locator)
        branch_name_element = self.driver.find_element(*branch_name_locator)
        if not branch_name_element.get_attribute("value"):
            fake_branch_name = "Branch " + company_data["name"]
            self.do_send_keys(branch_name_locator, fake_branch_name)

        self.do_click(self.locators.FILL_SAME_COMPANY_BUTTON)
        self.do_click(self.locators.AGREE_TERMS_CHECKBOX)
        self.do_click(self.locators.REGISTER_BUTTON)

    def create_company(self, company_data):
        """Encapsulates the company creation flow."""
        self.click_add_company()
        self.fill_registration_form1(company_data)
        self.fill_registration_form2()
        self.fill_registration_form3(company_data)

    def manage_newly_created_company(self, company_name):
        manage_button_locator = (self.locators.MANAGE_BUTTON_BY_NAME[0], self.locators.MANAGE_BUTTON_BY_NAME[1].format(company_name=company_name))
        self.do_click(manage_button_locator)

    def get_company_name_from_detail_page(self, company_name):
        company_name_header_locator = (self.locators.COMPANY_NAME_DETAIL_HEADER[0], self.locators.COMPANY_NAME_DETAIL_HEADER[1].format(company_name=company_name))
        try:
            company_name_text = self.get_text(company_name_header_locator)
            if company_name_text != company_name:
                self.driver.refresh()
                self.wait_for_element_visible(company_name_header_locator)
                company_name_text = self.get_text(company_name_header_locator)
        except Exception:
            self.driver.refresh()
            self.wait_for_element_visible(company_name_header_locator)
            company_name_text = self.get_text(company_name_header_locator)
        return company_name_text

    def verify_company_data_on_detail_page(self, company_data):
        """Confirm that the inputted company data is displayed correctly on the detail page."""
        company_name_locator = self.locators.COMPANY_NAME_INPUT
        company_name_element = self.driver.find_element(*company_name_locator)
        assert company_name_element.get_attribute("value") == company_data["name"], (
            f"Expected company name '{company_data['name']}', but got '{company_name_element.get_attribute('value')}'"
        )
