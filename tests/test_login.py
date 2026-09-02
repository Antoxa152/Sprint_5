import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestLogin:
    """Тесты для проверки разных сценариев входа в систему."""

    @staticmethod
    def _perform_login(driver, email, password):
        """Вспомогательный метод: выполнить вход (без ожидания)."""
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()

    @staticmethod
    def _assert_logged_in(driver, timeout=8):
        
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))

    def test_login_via_button_on_main_page(self, driver):
        """Вход по кнопке «Войти в аккаунт» на главной странице."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))

        self._perform_login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

    def test_login_via_personal_account(self, driver):
        """Вход через кнопку «Личный кабинет»."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))

        self._perform_login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

    def test_login_via_registration_form_button(self, driver):
        """Вход через кнопку в форме регистрации."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.login_button_main_page).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.register_link).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.submit_button))
        driver.find_element(*Locators.login_button_in_registration_form).click()

        self._perform_login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

    def test_login_via_password_recovery_button(self, driver):
        """Вход через кнопку в форме восстановления пароля."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))
        driver.find_element(*Locators.forgot_password_button).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.login_password_recovery_form_button))
        driver.find_element(*Locators.login_password_recovery_form_button).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.login_button))

        self._perform_login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)
        