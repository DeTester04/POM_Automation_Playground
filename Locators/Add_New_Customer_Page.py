from selenium.webdriver.common.by import By

class AddNewCustomerLocators:

    NEW_CUSTOMER_BUTTON = (By.ID, "new-customer")
    EMAIL = (By.ID, "EmailAddress")
    FIRST_NAME = (By.ID, "FirstName")
    LAST_NAME = (By.ID, "LastName")
    CITY = (By.ID, "City")
    STATE = (By.ID, "StateOrRegion")
    GENDER = (By.CSS_SELECTOR, "input[name='gender'][value='male']")
    ADD_TO_PROMOTIONAL_LIST = (By.NAME, "promos-name")
    SUBMIT_BUTTON = (By.CLASS_NAME, "btn-primary")

class LogoutLocators:
    LOG_OUT = (By.CLASS_NAME, "nav-link")