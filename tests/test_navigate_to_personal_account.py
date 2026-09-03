from pages.profile_page import ProfilePage


class TestPersonalAccountNavigation:
    

    def test_navigate_to_personal_account(self, profile_page):
        profile_page.open_profile()
        profile_page.assert_order_history_visible()
        