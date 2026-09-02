import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestPersonalAccountNavigation:
    """Тесты для проверки перехода в личный кабинет и отображения его элементов."""

    @staticmethod
    def _login(driver, email, password):
        """Вспомогательный метод: вход в систему (без ожидания маркера успеха)."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()

    @staticmethod
    def _assert_logged_in(driver, timeout=8):
        """Проверить, что пользователь успешно вошёл: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))

    @staticmethod
    def _assert_element_displayed(driver, locator, timeout=8):
        """Проверить, что элемент отображается: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(locator))

    def test_navigate_to_personal_account(self, driver):
        """Переход в личный кабинет по кнопке и проверка отображения истории заказов."""
        self._login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

        driver.find_element(*Locators.personal_account_button).click()
        self._assert_element_displayed(driver, Locators.profile)

        self._assert_element_displayed(driver, Locators.order_history)
        