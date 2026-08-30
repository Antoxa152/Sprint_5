import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


# Переход из раздела "Булки" в раздел "Начинки"
def test_navigate_buns_to_fillings(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'antoxa2709@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))

    # Клик по «Начинки»
    fillings_tab = driver.find_element(*Locators.fillings_section)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(fillings_tab))
    fillings_tab.click()

    # Ждём, пока активной станет вкладка «Начинки»
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.selected_section).text == "Начинки"
    )

    assert driver.find_element(*Locators.selected_section).text == "Начинки"


# Переход из раздела "Начинки" в раздел "Соусы"
def test_navigate_fillings_to_sauses(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'antoxa2709@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))

    # Сначала убеждаемся, что мы на «Начинках»
    fillings_tab = driver.find_element(*Locators.fillings_section)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(fillings_tab))
    fillings_tab.click()

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.selected_section).text == "Начинки"
    )

    # Теперь кликаем по «Соусы»
    sauces_tab = driver.find_element(*Locators.sauces_section)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_tab))
    sauces_tab.click()

    # Ждём, пока активной станет «Соусы»
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.selected_section).text == "Соусы"
    )

    assert driver.find_element(*Locators.selected_section).text == "Соусы"


# Переход из раздела "Соусы" в раздел "Булки"
def test_navigate_sausec_to_buns(driver):
    driver.get("https://stellarburgers.education-services.ru/")

    email = 'antoxa2709@yandex.ru'
    password = 'qwerty123'

    driver.find_element(*Locators.login_button_main_page).click()
    driver.find_element(*Locators.email_field).send_keys(email)
    driver.find_element(*Locators.password_field).send_keys(password)
    driver.find_element(*Locators.login_button).click()

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.make_an_order_button))

    # Переключаемся на «Соусы» и ждём, что они стали активными
    sauces_tab = driver.find_element(*Locators.sauces_section)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(sauces_tab))
    sauces_tab.click()

    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.selected_section).text == "Соусы"
    )

    # Теперь кликаем по «Булкам»
    buns_tab = driver.find_element(*Locators.buns_section)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(buns_tab))
    buns_tab.click()

    # Ждём, что активной стала «Булки»
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(*Locators.selected_section).text == "Булки"
    )

    assert driver.find_element(*Locators.selected_section).text == "Булки"
