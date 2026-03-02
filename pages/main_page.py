from typing import Tuple

from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


from config.params import URL_MAIN_PAGE
from locators.locators import MainPageLocators


class MainPage:
    def __init__(self, driver: WebDriver, wait=10):
        self.driver = driver
        self.url = driver.get(URL_MAIN_PAGE)
        self.wait = WebDriverWait(self.driver, wait)

    def _find_elements(self, by: By, locator: str) -> list[WebElement]:
        return self.wait.until(
            EC.presence_of_all_elements_located((by, locator))
        )

    def _check_if_element_displayed(
            self,
            locator: Tuple[By, str],
            element_name: str,
            min_expected: int = 1) -> None:

        elements = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
            )
        assert elements, f'{element_name} не отображается'

    def check_header_is_displayed(self) -> None:
        self._check_if_element_displayed(
            MainPageLocators.HEADER,
            'Хедер'
            )

    def check_navbar_is_displayed(self) -> None:
        self._check_if_element_displayed(
            MainPageLocators.NAVIGATION_BAR,
            'Блок навигации'
            )

    def check_courses_is_displayed(self) -> None:
        self._check_if_element_displayed(
            MainPageLocators.COURSES_LIST,
            'Список с курсами'
            )

    def check_footer_is_displayed(self) -> None:
        self._check_if_element_displayed(
            MainPageLocators.FOOTER,
            'Футер'
            )

    def check_contacts(self) -> None:
        contacts = self._find_elements(
            *MainPageLocators.HEADER_CONTACTS
        )
        assert all(
            contact.text for contact in contacts
            ), 'Не все контакты отображаются'
