from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        self.driver.get(base_url)

    def click_main_login_button(self):
        self.driver.find_element(*Locators.login_button_main_page).click()
        self.wait.until(EC.visibility_of_element_located(Locators.register_link))

    def click_personal_account_button(self):
        self.driver.find_element(*Locators.personal_account_button).click()
        self.wait.until(EC.visibility_of_element_located(Locators.register_link))

    def go_to_login_from_registration(self):
        self.driver.find_element(*Locators.register_link).click()
        self.wait.until(EC.visibility_of_element_located(Locators.submit_button))
        self.driver.find_element(*Locators.login_button_in_registration_form).click()
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))

    def go_to_login_from_recovery(self):
        self.driver.find_element(*Locators.forgot_password_button).click()
        self.wait.until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
        self.driver.find_element(*Locators.login_password_recovery_form_button).click()
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))

    def perform_login(self, email, password):
        self.driver.find_element(*Locators.email_field).send_keys(email)
        self.driver.find_element(*Locators.password_field).send_keys(password)
        self.driver.find_element(*Locators.login_button).click()

    def assert_logged_in(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))
        