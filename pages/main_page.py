from typing import Tuple

from selenium.common import TimeoutException
from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


from config.params import URL_MAIN_PAGE
from locators.locators import MainPageLocators
from utils.js_scripts import FOOTER_ADDRESS_SCRIPT
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

    def _check_if_element_visible(
            self,
            locator: Tuple[By, str]
            ) -> WebElement | None:
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
                )
        except TimeoutException:
            return None

    def _validate_phone_numbers(self, contacts: list[WebElement]) -> None:
        phone_numbers = [
            contact.text for contact in contacts
            if SC.is_phone_number(contact.text)
            ]
        assert phone_numbers, (
            'Hомера телефонов отсутствуют или не соответствуют формату.',
            f'Получен список значений {[x.text for x in contacts]}',
            f'Номера {phone_numbers}'
        )

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

    def close_popup(self) -> None:
        try:
            close_button = self.wait.until(
                EC.element_to_be_clickable(
                    MainPageLocators.CLOSE_POPUP
                )
            )
            close_button.click()
        except TimeoutException:
            pass

    def check_header_is_displayed(self) -> None:
        assert self._check_if_element_visible(
            MainPageLocators.HEADER
            ), 'Хедер не отображается'

    def check_navbar_is_displayed(self) -> None:
        assert self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
            ), 'Блок навигации не отображается'

    def check_courses_is_displayed(self) -> None:
        assert self._check_if_element_visible(
            MainPageLocators.COURSES_LIST
            ), 'Список с курсами не отображается'

    def check_footer_is_displayed(self) -> None:
        assert self._check_if_element_visible(
            MainPageLocators.FOOTER
            ), 'Футер не отображается'

    def check_contacts(self) -> None:
        contacts = self._find_elements(
            *MainPageLocators.HEADER_CONTACTS
        )
        assert all(
            contact.text for contact in contacts
            ), 'Не все контакты отображаются'

        self._validate_phone_numbers(contacts)
        self._validate_links(contacts, SC.is_skype, 'Skype')
        self._validate_links(contacts, SC.is_email_link, 'Email')

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

    def check_footer_address(self) -> None:
        address_element = self.wait.until(EC.visibility_of_element_located(
                (
                    MainPageLocators.FOOTER_ADDRESS
                )
            )
        )
        address = self.driver.execute_script(
            FOOTER_ADDRESS_SCRIPT, address_element
        )
        assert address, 'Адрес в футере не найден'

    def check_footer_phone_numbers(self) -> None:
        phone_numbers = self._find_elements(
            *MainPageLocators.FOOTER_PHONE_NUMBERS
        )
        self._validate_phone_numbers(phone_numbers)

    def check_footer_emails(self) -> None:
        emails = self._find_elements(
            *MainPageLocators.FOOTER_EMAILS
        )
        assert all(
            SC.is_email(email.text) for email in emails
        ), 'Не все имейлы соответствуют формату'

    def check_navbar_on_scroll(self, delta_x=0, delta_y=1000) -> None:
        navbar = self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
        )
        init_location = navbar.location

        self.close_popup()

        action = ActionChains(self.driver)
        action.scroll_by_amount(delta_x, delta_y).perform()

        navbar_after = self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
        )
        new_location = navbar_after.location

        assert init_location['y'] != new_location['y'], (
            'Позиция меню навигации не изменилась после скролла.'
        )
