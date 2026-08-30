import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data_randomizer import generate_name, generate_email, generate_password, generate_incorrect_password
from locators import Locators
from conftest import driver



# Позитивная проверка регистрации
def test_registration_positive(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    user_name = generate_name()
    user_email = generate_email()
    user_password = generate_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))

    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field).send_keys(user_email)
    driver.find_element(*Locators.password_field).send_keys(user_password)
    driver.find_element(*Locators.submit_button).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.login_button))

    assert driver.find_element(*Locators.register_link).is_displayed()


# Регистрация с невалидным паролем
def test_registration_incorrect_password_message(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    user_name = generate_name()
    user_email = generate_email()
    user_password = generate_incorrect_password()

    driver.find_element(*Locators.login_button_main_page).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.register_link))

    driver.find_element(*Locators.register_link).click()
    WebDriverWait(driver, 8).until(EC.visibility_of_element_located(Locators.submit_button))

    driver.find_element(*Locators.name_field).send_keys(user_name)
    driver.find_element(*Locators.email_field).send_keys(user_email)
    driver.find_element(*Locators.password_field).send_keys(user_password)
    driver.find_element(*Locators.submit_button).click()

    assert driver.find_element(*Locators.incorrect_password_message).text == 'Некорректный пароль'
