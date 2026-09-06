from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, base_url):
        """Открыть главную страницу."""
        self.driver.get(base_url)

    def _wait_and_click(self, locator):
        """Ждать элемент и кликнуть по нему (переиспользуемый хелпер)."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def click_main_login_button(self):
        """Клик по кнопке «Войти в аккаунт» на главной."""
        self._wait_and_click(Locators.login_button_main_page)
        self.wait.until(EC.visibility_of_element_located(Locators.register_link))

    def click_personal_account_button(self):
        """Клик по кнопке «Личный кабинет»."""
        self._wait_and_click(Locators.personal_account_button)
        self.wait.until(EC.visibility_of_element_located(Locators.register_link))

    def go_to_login_from_registration(self):
        """Перейти к форме входа со страницы регистрации."""
        self._wait_and_click(Locators.login_button_in_registration_form)
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))

    def go_to_login_from_recovery(self):
        """Перейти к форме входа из восстановления пароля."""
        self._wait_and_click(Locators.forgot_password_button)
        self.wait.until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
        self._wait_and_click(Locators.login_password_recovery_form_button)
        self.wait.until(EC.visibility_of_element_located(Locators.login_button))

    def perform_login(self, email, password):
        """Ввести email и пароль, нажать кнопку входа."""
        email_field = self.driver.find_element(*Locators.email_field)
        password_field = self.driver.find_element(*Locators.password_field)

        email_field.clear()
        email_field.send_keys(email)
        password_field.clear()
        password_field.send_keys(password)

        self._wait_and_click(Locators.login_button)

    def assert_logged_in(self, timeout=10):
        """Проверить, что пользователь залогинен (видна кнопка «Оформить заказ»)."""
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))
        