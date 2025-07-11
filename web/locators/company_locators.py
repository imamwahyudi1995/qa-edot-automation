from selenium.webdriver.common.by import By

class CompanyLocators:
    COMPANIES_NAV_LINK = (By.LINK_TEXT, "Companies")
    SETTING_NAV_LINK = (By.LINK_TEXT, "Settings")
    ADD_COMPANY_BUTTON = (By.XPATH, "//button[normalize-space()='+ Add Company']")
    COMPANY_NAME_INPUT = (By.XPATH, "//input[@placeholder='Input Company Name']")
    EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Input Email']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='Input Phone']")
    STREET_ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='Input Address']")
    INDUSTRY_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Industry Type']")
    INDUSTRY_OPTION = (By.XPATH, "//div[@data-value='construction']")
    COMPANY_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Company Type']")
    COMPANY_TYPE_OPTION = (By.XPATH, "//div[@data-value='importer/exporter']")
    LANGUAGE_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Language']")
    LANGUAGE_OPTION = (By.XPATH, "//div[@data-value='indonesia']")
    COUNTRY_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Country']")
    COUNTRY_OPTION = (By.XPATH, "//div[@data-value='id']")
    PROVINCE_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Province']")
    PROVINCE_OPTION = (By.XPATH, "//div[@data-value='v11']")
    CITY_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose City']")
    CITY_OPTION = (By.XPATH, "//div[@data-value='v1103']")
    DISTRICT_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose District']")
    DISTRICT_OPTION = (By.XPATH, "//div[@data-value='v110102']")
    SUB_DISTRICT_TYPE_DROPDOWN = (By.XPATH, "//button[normalize-space()='Choose Sub District']")
    SUB_DISTRICT_OPTION = (By.XPATH, "//div[@data-value='jambo manyang']")
    AGREE_TERMS_CHECKBOX = (By.XPATH, "//button[@id='select-all']")
    REGISTER_BUTTON = (By.XPATH, "//button[normalize-space()='Register']")
    NEXT_BUTTON = (By.XPATH, "//button[normalize-space()='Next']")
    FILL_SAME_COMPANY_BUTTON = (By.XPATH, "//button[contains(text(),'Fill in with the same data from the Company record')]")
    FORM_STEP_2 = (By.XPATH, "//span[normalize-space()='Register Legal & Bank']")
    MANAGE_BUTTON_BY_NAME = (By.XPATH, "//div[text()='{company_name}']/ancestor::div[contains(@class,'card')]//button[normalize-space()='Manage']")
    COMPANY_NAME_DETAIL_HEADER = (By.XPATH, "//span[normalize-space()='{company_name}']")
