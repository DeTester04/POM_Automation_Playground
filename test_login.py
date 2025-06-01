import pytest

from selenium import webdriver

from Action.Action_page import ActionPage, AddNewCustomerPage, LogoutPage
from config.Configuration import Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    #chrome_options.add_argument("--headless")      # Run in headless mode
    chrome_options.add_argument("--disable-gpu")   # Prevent GPU errors in headless mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(20)                     # Wait implicitly up to 20s
    driver.maximize_window()                       # Maximize window (has no effect in headless, but harmless)
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
    add_customer.enter_email(Config.EMAIL)
    add_customer.enter_first_name(Config.FIRST_NAME)
    add_customer.enter_last_name(Config.LAST_NAME)
    add_customer.enter_city(Config.CITY)
    add_customer.enter_state(Config.STATE)
    add_customer.click_gender()
    add_customer.click_add_to_promotional_list()
    add_customer.click_submit_button()

def test_logout_button(login):

    log_out = LogoutPage(login.driver)

 #Click logout button
    log_out.click_log_out()

