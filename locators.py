from selenium.webdriver.common.by import By

class Locators:
    login_button_main_page = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    register_link = (By.XPATH, '//a[text() = "Зарегистрироваться"]')

    submit_button = (By.XPATH, '//button[text() = "Зарегистрироваться"]')

    name_field = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

    email_field = (By.XPATH, './/label[text()="Email"]/following-sibling::input')

    password_field = (By.XPATH, './/label[text()="Пароль"]/following-sibling::input')

    login_button = (By.XPATH, './/button[text()="Войти"]')
    

    incorrect_password_message = (By.XPATH, '//p[text() = "Некорректный пароль"]')

    make_an_order_button = (By.XPATH, '//button[text()="Оформить заказ"]')

    personal_account_button = (By.XPATH, '//p[text() = "Личный Кабинет"]')

    login_button_in_registration_form = (By.XPATH, '//a[text() = "Войти"]')

    forgot_password_button = (By.XPATH, '//a[text() = "Восстановить пароль"]')

    login_password_recovery_form_button = (By.XPATH, '//a[text() = "Войти"]')

    profile = (By.XPATH, '//a[@href = "/account/profile"]')

    order_history = (By.XPATH, '//a[@href = "/account/order-history"]')

    constructor_button_in_header = (By.XPATH, '//p[text() = "Конструктор"]')

    logo = (By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]')

    logout_button = (By.XPATH, '//button[@type = "button"]')

    buns_section = (By.XPATH, '//span[text() = "Булки"]')

    sauces_section = (By.XPATH, '//span[text() = "Соусы"]')

    fillings_section = (By.XPATH, '//span[text() = "Начинки"]')

    selected_section = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
    