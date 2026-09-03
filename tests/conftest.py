import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)

if project_root not in sys.path:
    sys.path.insert(0, project_root)

import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage  # <-- вот этого импорта не хватало!
from config import BASE_URL
from data import TEST_EMAIL, TEST_PASSWORD

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def driver_with_auth(driver):
    page = LoginPage(driver)
    page.open(BASE_URL)
    page.click_main_login_button()
    page.perform_login(TEST_EMAIL, TEST_PASSWORD)
    page.assert_logged_in()
    return driver

@pytest.fixture
def profile_page(driver_with_auth):
    return ProfilePage(driver_with_auth)

