from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL 

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def _wait_and_click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def open_registration_form(self):
        self.driver.get(BASE_URL) 
        self._wait_and_click(Locators.register_link)

    def register(self, name, email, password):
        name_field = self.driver.find_element(*Locators.name_field)
        email_field = self.driver.find_element(*Locators.email_field)
        password_field = self.driver.find_element(*Locators.password_field)

        name_field.clear()
        name_field.send_keys(name)
        email_field.clear()
        email_field.send_keys(email)
        password_field.clear()
        password_field.send_keys(password)

        submit_btn = self.driver.find_element(*Locators.submit_button)
        self.wait.until(EC.element_to_be_clickable(submit_btn))
        submit_btn.click()

    def assert_registration_success(self):
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))

    def assert_incorrect_password_message(self):
        self.wait.until(EC.visibility_of_element_located(Locators.error_message))
