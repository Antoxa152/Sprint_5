from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class ConstructorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_section(self, section_locator, expected_title):
        """Перейти к секции и проверить её заголовок."""
        section_tab = self.driver.find_element(*section_locator)
        self.wait.until(EC.element_to_be_clickable(section_tab))
        section_tab.click()
        self._assert_section_title(expected_title)

    def _assert_section_title(self, expected_title, timeout=10):
        """Проверить, что заголовок секции равен ожидаемому."""
        wait = WebDriverWait(self.driver, timeout)
        assert wait.until(
            lambda d: d.find_element(*Locators.selected_section).text == expected_title
        )
        