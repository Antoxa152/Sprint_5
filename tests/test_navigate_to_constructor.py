import pytest
from pages.profile_page import ProfilePage

class TestNavigationFromProfile:
    

    def test_navigate_via_constructor_button(self, profile_page):
        
        """Переход в конструктор по кнопке «Конструктор» в шапке."""
        profile_page.open_profile()
        profile_page.navigate_to_constructor_via_button()
        profile_page.assert_in_constructor()

    def test_navigate_via_logo(self, profile_page):
        """Переход в конструктор по клику на логотип Stellar Burgers."""
        profile_page.open_profile()
        profile_page.navigate_to_constructor_via_logo()
        profile_page.assert_in_constructor()