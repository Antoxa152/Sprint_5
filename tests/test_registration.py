import pytest
from data_randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from pages.register_page import RegisterPage


class TestRegistration:
    """Тесты для проверки регистрации пользователя."""

    def test_registration_positive(self, register_page):
        """Позитивный сценарий: успешная регистрация нового пользователя."""
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_password()

        register_page.open_registration_form()
        register_page.register(user_name, user_email, user_password)
        register_page.assert_registration_success()

    def test_registration_incorrect_password_message(self, register_page):
        """Негативный сценарий: проверка сообщения об ошибке при некорректном пароле."""
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_incorrect_password()

        register_page.open_registration_form()
        register_page.register(user_name, user_email, user_password)
        register_page.assert_incorrect_password_message()