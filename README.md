# POM_Automation_Playground

Setting up POM
Create virtual environment 
Commandline to create requirements.txt - pip freeze > requirements.txt
Commandline Install Selenium - pip install selenium
Commandline used to install two Python packages: pip install selenium pytest
pip install pytest-htm

✅ 1. selenium
A browser automation framework.

Allows you to control web browsers through programs for testing web applications.

Often used in automated UI testing.

✅ 2. pytest
A powerful testing framework for Python.

Used for writing and running unit tests, functional tests, or even end-to-end tests.

My_Selenium_Project/
│
├── locators/
│   └── login_locators.py
│
├── actions/
│   └── login_actions.py
│
├── tests/
│   └── test_login.py
│
├── requirements.txt
└── conftest.py (for pytest setup, if using pytest)


from selenium.webdriver.common.by import By

class LoginLocators:
    EMAIL_INPUT = (By.ID, "email-id")
    PASSWORD_INPUT = (By.ID, "password")
    REMEMBER_ME_CHECKBOX = (By.ID, "remember")
    LOGIN_BUTTON = (By.ID, "submit-id")
    ADD_CUSTOMER_BTN = (By.ID, "new-customer")

from locators.login_locators import LoginLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located(LoginLocators.EMAIL_INPUT)).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD_INPUT).send_keys(password)

    def click_remember_me(self):
        self.driver.find_element(*LoginLocators.REMEMBER_ME_CHECKBOX).click()

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def click_add_customer(self):
        self.wait.until(EC.element_to_be_clickable(LoginLocators.ADD_CUSTOMER_BTN)).click()

import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


