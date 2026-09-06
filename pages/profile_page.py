from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class ProfilePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_profile(self):
        self.driver.find_element(*Locators.personal_account_button).click()
        self.wait.until(EC.visibility_of_element_located(Locators.profile))

    def perform_logout(self):
        self.driver.find_element(*Locators.logout_button).click()

    def assert_logged_out(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(Locators.login_button))

    def navigate_to_constructor_via_button(self):
        btn = self.driver.find_element(*Locators.constructor_button_in_header)
        self.wait.until(EC.element_to_be_clickable(btn))
        btn.click()

    def navigate_to_constructor_via_logo(self):
        logo = self.driver.find_element(*Locators.logo)
        self.wait.until(EC.element_to_be_clickable(logo))
        logo.click()

    def assert_in_constructor(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))

    def assert_order_history_visible(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(Locators.order_history))
        