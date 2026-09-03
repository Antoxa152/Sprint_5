from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_registration_form(self):
        self.driver.get(Locators.BASE_URL)  # если BASE_URL есть в locators, иначе из config
        self.driver.find_element(*Locators.login_button_main_page).click()
        self.wait.until(EC.visibility_of_element_located(Locators.register_link))
        self.driver.find_element(*Locators.register_link).click()
        self.wait.until(EC.visibility_of_element_located(Locators.submit_button))

    def register(self, name, email, password):
        self.driver.find_element(*Locators.name_field).send_keys(name)
        self.driver.find_element(*Locators.email_field).send_keys(email)
        self.driver.find_element(*Locators.password_field).send_keys(password)
        self.driver.find_element(*Locators.submit_button).click()

    def assert_registration_success(self):
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))
        assert self.driver.find_element(*Locators.register_link).is_displayed()

    def assert_incorrect_password_message(self, expected_message='Некорректный пароль'):
        message_element = self.wait.until(
            EC.visibility_of_element_located(Locators.incorrect_password_message)
        )
        assert message_element.text == expected_message