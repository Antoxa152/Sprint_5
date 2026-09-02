import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestLogout:
    """Тесты для сценария выхода из учётной записи."""

    @staticmethod
    def _perform_login(driver, email, password):
        """Вспомогательный метод: выполнить вход (без ожидания)."""
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()

    @staticmethod
    def _assert_logged_in(driver, timeout=8):
        """Проверить, что пользователь успешно вошёл: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))

    @staticmethod
    def _assert_logged_out(driver, timeout=8):
        """Проверить, что пользователь вышел из системы: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(Locators.login_button))

    def test_logout(self, driver):
        """Проверка выхода из учётной записи через кнопку в профиле."""
        driver.get(BASE_URL)

        driver.find_element(*Locators.login_button_main_page).click()
        self._perform_login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

        driver.find_element(*Locators.personal_account_button).click()
        WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logout_button).click()

        self._assert_logged_out(driver)
        