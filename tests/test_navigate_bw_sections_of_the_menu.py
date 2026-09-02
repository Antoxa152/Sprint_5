import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestNavigation:
    """Тесты для проверки навигации между секциями конструктора бургеров."""

    @staticmethod
    def _login(driver, email, password):
        """Вспомогательный метод для входа в систему (без ожидания маркера успеха)."""
        driver.find_element(*Locators.login_button_main_page).click()
        driver.find_element(*Locators.email_field).send_keys(email)
        driver.find_element(*Locators.password_field).send_keys(password)
        driver.find_element(*Locators.login_button).click()

    @staticmethod
    def _assert_logged_in(driver, timeout=10):
        """Проверить, что пользователь успешно вошёл: ждём и проверяем кнопку «Оформить заказ» в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(EC.visibility_of_element_located(Locators.make_an_order_button))

    @staticmethod
    def _assert_section_title(driver, expected_title, timeout=10):
        """Проверить, что заголовок секции равен ожидаемому: ожидание инкапсулировано в ассерте."""
        wait = WebDriverWait(driver, timeout)
        assert wait.until(lambda d: d.find_element(*Locators.selected_section).text == expected_title)

    def test_navigate_buns_to_fillings(self, driver):
        """Переход из раздела «Булки» в раздел «Начинки»."""
        driver.get(BASE_URL)
        self._login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

        fillings_tab = driver.find_element(*Locators.fillings_section)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(fillings_tab))
        fillings_tab.click()

        self._assert_section_title(driver, "Начинки")

    def test_navigate_fillings_to_sauces(self, driver):
        """Переход из раздела «Начинки» в раздел «Соусы»."""
        driver.get(BASE_URL)
        self._login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

        fillings_tab = driver.find_element(*Locators.fillings_section)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(fillings_tab))
        fillings_tab.click()
        self._assert_section_title(driver, "Начинки")

        sauces_tab = driver.find_element(*Locators.sauces_section)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_tab))
        sauces_tab.click()

        self._assert_section_title(driver, "Соусы")

    def test_navigate_sauces_to_buns(self, driver):
        """Переход из раздела «Соусы» в раздел «Булки»."""
        driver.get(BASE_URL)
        self._login(driver, TEST_EMAIL, TEST_PASSWORD)
        self._assert_logged_in(driver)

        sauces_tab = driver.find_element(*Locators.sauces_section)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_tab))
        sauces_tab.click()
        self._assert_section_title(driver, "Соусы")

        buns_tab = driver.find_element(*Locators.buns_section)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(buns_tab))
        buns_tab.click()

        self._assert_section_title(driver, "Булки")
        