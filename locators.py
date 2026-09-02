from selenium.webdriver.common.by import By

class Locators:
    # Кнопка "Войти в аккаунт" на главной странице
    login_button_main_page = (By.XPATH, './/button[text() = "Войти в аккаунт"]')

    # Ссылка "Зарегистрироваться"
    register_link = (By.XPATH, '//a[text() = "Зарегистрироваться"]')

    # Кнопка "Зарегистрироваться"
    submit_button = (By.XPATH, '//button[text() = "Зарегистрироваться"]')

    # Поле "Имя"
    name_field = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')

    # Поле "Email"
    email_field = (By.XPATH, './/label[text()="Email"]/following-sibling::input')

    # Поле "Пароль"
    password_field = (By.XPATH, './/input[@name="Пароль"]')

    # Кнопка "Войти"
    login_button = (By.XPATH, './/button[text()="Войти"]')
    

    # Сообщение об ошибке "Некорректный пароль"
    incorrect_password_message = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Кнопка "Оформить заказ"
    make_an_order_button = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Личный кабинет"
    personal_account_button = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Войти" на форме регистрации
    login_button_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

    # Кнопка "Восстановить пароль"
    forgot_password_button = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка "Войти" в форме восстановления пароля
    login_password_recovery_form_button = By.XPATH, '//a[text() = "Войти"]'

    # Раздел "Профиль"
    profile = By.XPATH, '//a[@href = "/account/profile"]'

    # Раздел "История заказов"
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка "Конструктор" в шапке сайта
    constructor_button_in_header = By.XPATH, '//p[text() = "Конструктор"]'

    # Лого в шапке сайта
    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'

    # Кнопка "Выйти"
    logout_button = By.XPATH, '//button[@type = "button"]'

    # Заголовок раздела "Булки"
    buns_section = By.XPATH, '//span[text() = "Булки"]'

    # Заголовок раздела "Соусы"
    sauces_section = By.XPATH, '//span[text() = "Соусы"]'


    # Заголовок раздела "Начинки"
    fillings_section = By.XPATH, '//span[text() = "Начинки"]'

    # Активный раздел конструктора
    selected_section = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')
    