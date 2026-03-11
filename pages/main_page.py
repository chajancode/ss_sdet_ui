from selenium.common import TimeoutException
from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement


from config.params import URL_MAIN_PAGE
from locators.locators import LifetimeMembershipPageLocators, MainPageLocators
from pages.base_page import BasePage
from utils.js_scripts import FOOTER_ADDRESS_SCRIPT
from utils.string_checkers import StringChecker as SC


class MainPage(BasePage):
    """
    Главная страница веб‑приложения.

    Предоставляет методы для проверки основных элементов интерфейса:
    хедера, футера, навигации, контактов и социальных сетей.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует главную страницу.

        **Args:**
            - `driver (WebDriver)`: Экземпляр класса WebDriver для 
            управления браузером.
        """
        super().__init__(driver)
        self.url = driver.get(URL_MAIN_PAGE)

    def _validate_phone_numbers(self, contacts: list[WebElement]) -> None:
        """
        Проверяет наличие и корректность номеров телефонов в списке контактов.

        Извлекает тексты элементов и фильтрует их по формату номера телефона.

        **Args:**
            - `contacts (list[WebElement])`: Список веб‑элементов с
            контактными данными.

        **Raises:**
            - `AssertionError`: Если номера телефонов отсутствуют или не
            соответствуют формату.
        """
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
        """
        Проверяет наличие валидных ссылок в списке элементов.

        Фильтрует элементы по наличию атрибута `href` и результату
        валидации.

        **Args:**
            - `links (list[WebElement])`: Список веб‑элементов со ссылками.
            - `validator (SC)`: Функция‑валидатор для проверки формата
            ссылки.
            - `link_type (str)`: Тип ссылки для сообщения об ошибке
            (например, «Skype»).

        **Raises:**
            - `AssertionError`: Если валидные ссылки не найдены.
        """
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
        """
        Проверяет валидность отдельной ссылки.

        Получает атрибут `href` элемента и проверяет его через валидатор.

        **Args:**
            - `element (WebElement)`: Веб‑элемент со ссылкой.
            - `validator (SC)`: Функция‑валидатор для проверки формата
            ссылки.
            - `link_type (str)`: Тип ссылки для сообщения об ошибке.

        **Raises:**
            - `AssertionError`: Если ссылка отсутствует или не проходит
            валидацию.
        """
        href = element.get_attribute('href')
        assert href and validator(href), f'Ссылка на {link_type} не найдена'

    def close_popup(self) -> None:
        """
        Закрывает всплывающее окно, если оно присутствует.

        Пытается найти и кликнуть по кнопке закрытия. Если элемент не
        найден в течение таймаута, игнорирует ошибку.
        """
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
        """
        Проверяет видимость хедера страницы.

        Убеждается, что хедер отображается на странице.

        **Raises:**
            - `AssertionError`: Если хедер не отображается.
        """
        assert self._check_if_element_visible(
            MainPageLocators.HEADER
            ), 'Хедер не отображается'

    def check_navbar_is_displayed(self) -> None:
        """
        Проверяет видимость блока навигации.

        Убеждается, что навигационная панель отображается на странице.

        **Raises:**
            - `AssertionError`: Если блок навигации не отображается.
        """
        assert self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
            ), 'Блок навигации не отображается'

    def check_courses_is_displayed(self) -> None:
        """
        Проверяет видимость списка курсов.

        Убеждается, что список курсов отображается на странице.

        **Raises:**
            - `AssertionError`: Если список курсов не отображается.
        """
        assert self._check_if_element_visible(
            MainPageLocators.COURSES_LIST
            ), 'Список с курсами не отображается'

    def check_footer_is_displayed(self) -> None:
        """
        Проверяет видимость футера страницы.

        Убеждается, что футер отображается на странице.

        **Raises:**
            - `AssertionError`: Если футер не отображается.
        """
        assert self._check_if_element_visible(
            MainPageLocators.FOOTER
            ), 'Футер не отображается'

    def check_contacts(self) -> None:
        """
        Проверяет отображение и валидность контактных данных в хедере.

        Проверяет:
        - видимость всех контактов;
        - наличие номеров телефонов;
        - валидность ссылок на Skype и Email.

        **Raises:**
            - `AssertionError`: Если контакты не отображаются или не
            проходят валидацию.
        """
        contacts = self._find_elements(
            MainPageLocators.HEADER_CONTACTS
        )
        assert all(
            contact.text for contact in contacts
            ), 'Не все контакты отображаются'

        self._validate_phone_numbers(contacts)
        self._validate_links(contacts, SC.is_skype, 'Skype')
        self._validate_links(contacts, SC.is_email_link, 'Email')

    def check_social_media(self) -> None:
        """
        Проверяет отображение и валидность ссылок на социальные сети.

        Убеждается, что:
        - все элементы соцсетей найдены;
        - у всех есть атрибут `href`;
        - ссылки проходят валидацию по формату соцсетей.

        **Raises:**
            - `AssertionError`: Если соцсети не найдены или ссылки невалидны.
        """
        social_media = self._find_elements(
            MainPageLocators.HEADER_SOCIAL_MEDIA
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
        """
        Проверяет наличие адреса в футере.

        Использует JS-скрипт для получения текста адреса.

        **Raises:**
            - `AssertionError`: Если адрес не найден.
        """
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
        """
        Проверяет номера телефонов в футере.

        Находит элементы с номерами телефонов и проверяет их валидность.

        **Raises:**
            - `AssertionError`: Если номера не соответствуют формату.
        """
        phone_numbers = self._find_elements(
            MainPageLocators.FOOTER_PHONE_NUMBERS
        )
        self._validate_phone_numbers(phone_numbers)

    def check_footer_emails(self) -> None:
        """
        Проверяет валидность email-адресов в футере.

        Находит элементы с email-адресами и убеждается, что все они
        соответствуют формату email.

        **Raises:**
            - `AssertionError`: Если какой‑либо email не соответствует формату.
        """
        emails = self._find_elements(
            MainPageLocators.FOOTER_EMAILS
        )
        assert all(
            SC.is_email(email.text) for email in emails
        ), 'Не все имейлы соответствуют формату'

    def check_navbar_on_scroll(self, delta_x=0, delta_y=1000) -> None:
        """
        Проверяет фиксацию навигационной панели при скролле.

        Выполняет скролл страницы на `delta_y` пикселей и убеждается, что
        позиция навигационной панели не изменилась (панель зафиксирована).

        **Args:**
            - `delta_x (int, optional)`: Смещение по горизонтали.
            По умолчанию — 0.
            - `delta_y (int, optional)`: Смещение по вертикали.
            По умолчанию — 1000 px.

        **Raises:**
            - `AssertionError`: Если позиция меню навигации изменилась после скролла.
        """
        navbar = self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
        )
        init_location = navbar.location

        action = ActionChains(self.driver)
        action.scroll_by_amount(delta_x, delta_y).perform()

        navbar_after = self._check_if_element_visible(
            MainPageLocators.NAVIGATION_BAR
        )
        new_location = navbar_after.location

        assert init_location['y'] == new_location['y'], (
            'Позиция меню навигации не изменилась после скролла.'
        )

    def check_navigation_through_navbar(self) -> None:
        """
        Проверяет навигацию по сайту через меню в хедере.

        Выполняет следующие действия:
        1. Закрывает всплывающее окно (если есть).
        2. Кликает по пункту «All courses».
        3. Кликает по подпункту «Lifetime Membership».
        4. Проверяет, что открылся раздел «Lifetime Membership Club».
        5. Убеждается, что заголовок страницы соответствует ожидаемому.

        **Raises:**
            - `AssertionError`: Если:
                * пункт меню недоступен;
                * заголовок страницы не соответствует ожидаемому 
                («LIFETIME MEMBERSHIP CLUB»).
        """
        self.close_popup()

        all_courses = self._click_element(
            MainPageLocators.NAVBAR_ALL_COURSES
        )
        assert all_courses, 'Пункт меню "All courses" не доступен'

        lifetime_membership = self._click_element(
            MainPageLocators.NAVBAR_LIFETIME_MEMBERSHIP
        )
        assert lifetime_membership, (
            'Пункт меню "All Courses > Lifetime Membership" '
            'не доступен'
        )

        self.wait.until(EC.presence_of_all_elements_located(
            ((By.TAG_NAME, 'body'))
        ))
        page_title = self._find_element(
            LifetimeMembershipPageLocators.HEADING_TITLE
        )
        assert page_title.text == 'LIFETIME MEMBERSHIP CLUB', (
            f'Заголовок не соответствует ожидаемому. '
            f'Получен: {page_title}'
        )
