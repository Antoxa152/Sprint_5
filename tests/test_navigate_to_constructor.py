import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from conftest import driver


# Переход по клику на «Конструктор»
def test_navigate_to_constructor_to_personal_account_via_constructor_button(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'antoxa2709@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    driver.find_element(*Locators.constructor_button_in_header).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()

# Переход по клику на логотип Stellar Burgers
def test_navigate_to_constructor_to_personal_account_via_constructor_logo(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'antoxa2709@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()
    driver.find_element(*Locators.personal_account_button).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.profile))
    driver.find_element(*Locators.logo).click()
    WebDriverWait(driver, 6).until(EC.visibility_of_element_located(Locators.make_an_order_button))
    assert driver.find_element(*Locators.make_an_order_button).is_displayed()