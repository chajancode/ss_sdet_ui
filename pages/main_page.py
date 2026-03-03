from typing import Tuple

from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


from config.params import URL_MAIN_PAGE
from locators.locators import MainPageLocators
from utils.string_checkers import StringChecker as SC


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
            ) -> None:

        elements = self.wait.until(
            EC.visibility_of_all_elements_located(locator)
            )
        assert elements, f'{element_name} не отображается'

    def _validate_phone_numbers(self, contacts: list[WebElement]) -> None:
        phone_numbers = [
            contact.text for contact in contacts
            if SC.is_phone_number(contact.text)
            ]
        assert phone_numbers, 'номера телефонов отсутствуют'

    def _validate_links(
            self,
            links: list[WebElement],
            validator: SC,
            link_type: str
            ) -> None:
        valid_links = [
            link for link in links
            if link.get_attribute('href') and validator(
                link.get_attribute('href')
            )
        ]
        assert valid_links, f'Ссылка на {link_type} не найдена'

    def _validate_single_link(
            self,
            element: WebElement,
            validator: SC,
            link_type: str
            ) -> None:
        href = element.get_attribute('href')
        assert href and validator(href), f'Ссылка на {link_type} не найдена'

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

        self._validate_phone_numbers(contacts)
        self._validate_links(contacts, SC.is_skype, 'Skype')
        self._validate_links(contacts, SC.is_email, 'Email')

    def check_social_media(self) -> None:
        social_media = self._find_elements(
            *MainPageLocators.HEADER_SOCIAL_MEDIA
        )
        assert social_media, 'Социальные сети не найдены'

        assert all(
            link.get_attribute('href') for link in social_media
        ), 'Не все ссылки присутствуют'

        for link in social_media:
            self._validate_single_link(
                link, SC.is_social_media, link.get_attribute('aria-label')
            )
