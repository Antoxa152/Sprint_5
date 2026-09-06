import pytest
from pages.profile_page import ProfilePage

class TestLogout:
    

    def test_logout(self, profile_page):
        profile_page.open_profile()
        profile_page.perform_logout()
        profile_page.assert_logged_out()
        