import pytest
from pages.login_page import LoginPage
from pages.constructor_page import ConstructorPage

from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD


class TestNavigation:
    """Тесты для проверки навигации между секциями конструктора бургеров."""

    def test_navigate_buns_to_fillings(self, driver):
        """Переход из раздела «Булки» в раздел «Начинки»."""
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        login_page.open(BASE_URL)
        login_page.click_main_login_button()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

        constructor_page.navigate_to_section(Locators.fillings_section, "Начинки")

    def test_navigate_fillings_to_sauces(self, driver):
        """Переход из раздела «Начинки» в раздел «Соусы»."""
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        login_page.open(BASE_URL)
        login_page.click_main_login_button()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

        constructor_page.navigate_to_section(Locators.fillings_section, "Начинки")
        constructor_page.navigate_to_section(Locators.sauces_section, "Соусы")

    def test_navigate_sauces_to_buns(self, driver):
        """Переход из раздела «Соусы» в раздел «Булки»."""
        login_page = LoginPage(driver)
        constructor_page = ConstructorPage(driver)

        login_page.open(BASE_URL)
        login_page.click_main_login_button()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

        constructor_page.navigate_to_section(Locators.sauces_section, "Соусы")
        constructor_page.navigate_to_section(Locators.buns_section, "Булки")
        
        