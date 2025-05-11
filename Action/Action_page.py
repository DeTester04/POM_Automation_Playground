import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Locators.Add_New_Customer_Page import AddNewCustomerLocators, LogoutLocators
from Locators.Login_Page import LoginLocators

#Time Variable
DEFAULT_SLEEP_TIME = 5

class ActionPage:
    #Initializing our browser
    def __init__(self, driver):
        self.driver = driver

#calling our URL

    def open_login_page(self, url):
        self.driver.get(url)

#LOG IN PAGE

    def enter_email_address(self, email_address):
        enter_email_address = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.EMAIL_ADDRESS))
        enter_email_address.send_keys(email_address)
        time.sleep(DEFAULT_SLEEP_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(DEFAULT_SLEEP_TIME)

    def click_submit_button(self):
        click_submit_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LoginLocators.SUBMIT_BUTTON))
        click_submit_button.click()
        time.sleep(DEFAULT_SLEEP_TIME)


#HOMEPAGE/ADD CUSTOMER PAGE


class AddNewCustomerPage:
        # Initializing our browser
        def __init__(self, driver):
            self.driver = driver

        def click_new_customer_button(self):
            click_new_customer_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.NEW_CUSTOMER_BUTTON))
            click_new_customer_button.click()
            time.sleep(DEFAULT_SLEEP_TIME)


        def enter_email(self, email):
            enter_email = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.EMAIL))
            enter_email.send_keys(email)
            time.sleep(DEFAULT_SLEEP_TIME)

        def enter_first_name(self, first_name):
            enter_first_name = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.FIRST_NAME))
            enter_first_name.send_keys(first_name)
            time.sleep(DEFAULT_SLEEP_TIME)


        def enter_last_name(self, last_name):
            enter_last_name = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.LAST_NAME))
            enter_last_name.send_keys(last_name)
            time.sleep(DEFAULT_SLEEP_TIME)

        def enter_city(self, city):
            enter_city = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.CITY))
            enter_city.send_keys(city)
            time.sleep(DEFAULT_SLEEP_TIME)

        def enter_state(self, state):
            enter_state = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.STATE))
            enter_state.send_keys(state)
            time.sleep(DEFAULT_SLEEP_TIME)

        def click_gender(self):
            click_gender = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.GENDER))
            click_gender.click()
            time.sleep(DEFAULT_SLEEP_TIME)

        def click_add_to_promotional_list(self):
            click_add_to_promotional_list = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.ADD_TO_PROMOTIONAL_LIST))
            click_add_to_promotional_list.click()
            time.sleep(DEFAULT_SLEEP_TIME)

        def click_submit_button(self):
            click_submit_button = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(AddNewCustomerLocators.SUBMIT_BUTTON))
            click_submit_button.click()
            time.sleep(DEFAULT_SLEEP_TIME)

#LOG OUT BUTTON

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver

    def click_log_out(self):
        click_log_out = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located(LogoutLocators.LOG_OUT))
        click_log_out.click()
        time.sleep(DEFAULT_SLEEP_TIME)


