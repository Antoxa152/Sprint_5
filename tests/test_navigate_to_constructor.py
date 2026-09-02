import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestNavigationFromProfile:
    """Тесты для проверки навигации из личного кабинета обратно в конструктор."""

    @staticmethod
    def _login_and_go_to_profile(driver, email, password):
        """Вспомогательный метод: вход в систему и переход в личный кабинет (без ожиданий)."""
        driver.get(BASE_URL)
        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()

        driver.find_element(*Locators.personal_account_button).click()
        # Ожидание убрано: его место — в ассерте в тесте или отдельном _assert_* методе

    @staticmethod
    def _assert_element_visible(driver, locator, timeout=8):
        """Проверить, что элемент виден: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(locator))

    def test_navigate_via_constructor_button(self, driver):
        """Переход в конструктор по кнопке «Конструктор» в шапке."""
        self._login_and_go_to_profile(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_element_visible(driver, Locators.profile)

        driver.find_element(*Locators.constructor_button_in_header).click()
        self._assert_element_visible(driver, Locators.make_an_order_button)

    def test_navigate_via_logo(self, driver):
        """Переход в конструктор по клику на логотип Stellar Burgers."""
        self._login_and_go_to_profile(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_element_visible(driver, Locators.profile)

        driver.find_element(*Locators.logo).click()
        self._assert_element_visible(driver, Locators.make_an_order_button)
        