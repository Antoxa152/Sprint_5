import pytest
from data_randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from pages.register_page import RegisterPage


class TestRegistration:

    def test_registration_positive(self, register_page):
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_password()

        register_page.register(user_name, user_email, user_password)
        register_page.assert_registration_success()

    def test_registration_incorrect_password_message(self, register_page):
        user_name = generate_name()
        user_email = generate_email()
        user_password = generate_incorrect_password()

        register_page.register(user_name, user_email, user_password)
        register_page.assert_incorrect_password_message()
