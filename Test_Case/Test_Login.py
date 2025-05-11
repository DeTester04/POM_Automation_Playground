import pytest

from selenium import webdriver

from Action.Action_page import ActionPage, AddNewCustomerPage, LogoutPage
from config.Configuration import Config


@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = ActionPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

#log in page
def test_login_page_on_automation_play_ground_website(login):
    login.enter_email_address(Config.EMAIL_ADDRESS)
    login.enter_password(Config.PASSWORD)
    login.click_submit_button()

#Homepage/Add Customer Button
def test_add_customer_button(login):

    add_customer =  AddNewCustomerPage(login.driver)

#Homepage - Add Customer Button
    add_customer.click_new_customer_button()

#Add New Customer Form
    add_customer.enter_email("john@yopmail.com")
    add_customer.enter_first_name("John")
    add_customer.enter_last_name("Doe")
    add_customer.enter_city("New York")
    add_customer.enter_state("Maryland")
    add_customer.click_gender()
    add_customer.click_add_to_promotional_list()
    add_customer.click_submit_button()

def test_logout_button(login):

    log_out = LogoutPage(login.driver)

 #Click logout button
    log_out.click_log_out()

