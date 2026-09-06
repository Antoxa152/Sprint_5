import pytest
from pages.login_page import LoginPage
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD

class TestLogin:
    """Тесты для проверки разных сценариев входа в систему."""

    def test_login_via_button_on_main_page(self, login_page):
        """Вход по кнопке «Войти в аккаунт» на главной странице."""
        login_page.click_main_login_button()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

    def test_login_via_personal_account(self, login_page):
        """Вход через кнопку «Личный кабинет»."""
        login_page.click_personal_account_button()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

    def test_login_via_registration_form_button(self, login_page):
        """Вход через кнопку в форме регистрации."""
        login_page.click_main_login_button()
        login_page.go_to_login_from_registration()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()

    def test_login_via_password_recovery_button(self, login_page):
        """Вход через кнопку в форме восстановления пароля."""
        login_page.click_personal_account_button()
        login_page.go_to_login_from_recovery()
        login_page.perform_login(TEST_EMAIL, TEST_PASSWORD)
        login_page.assert_logged_in()
        