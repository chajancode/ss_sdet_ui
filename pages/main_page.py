import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from config.pages_urls import URL_MAIN_PAGE
from locators.lifetime_membership_page_locators import (
                            LifetimeMembershipPageLocators
)
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Главная страница веб‑приложения.

    Предоставляет методы для проверки основных элементов интерфейса:
    хедера, футера, навигации, контактов и социальных сетей.
    """
    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует главную страницу.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver для
            управления браузером

        Returns:
            None
        """
        super().__init__(driver)

    @allure.step('Открыть главную страницу.')
    def open(self) -> None:
        """
        Открывает главную страницу.

        Returns:
            None
        """
        self.driver.get(URL_MAIN_PAGE)
        self.close_popup()

    @property
    def current_url(self) -> str:
        """
        Возвращает текущий url.
        """
        return self.driver.current_url

    @allure.step('Закрыть всплывающее окно при его появлении.')
    def close_popup(self) -> None:
        """
        Закрывает всплывающее окно, если оно присутствует.

        Пытается найти и кликнуть по кнопке закрытия. Если элемент не
        найден в течение таймаута, игнорирует ошибку.

        Returns:
            None
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

    @allure.step('Проверить отображение хедера.')
    def is_header_displayed(self) -> bool:
        """
        Проверяет видимость хедера страницы.

        Returns:
            bool
        """
        return self.check_if_element_visible(MainPageLocators.HEADER)

    @allure.step('Проверить отображение блока навигации.')
    def is_navbar_displayed(self) -> bool:
        """
        Проверяет видимость блока навигации.

        Returns:
            bool
        """
        return self.check_if_element_visible(MainPageLocators.NAVIGATION_BAR)

    @allure.step('Проверить отображение списка курсов.')
    def is_courses_displayed(self) -> bool:
        """
        Проверяет видимость списка курсов.

        Returns:
            bool
        """
        return self.check_if_element_visible(MainPageLocators.COURSES_LIST)

    @allure.step('Проверить отображение футера.')
    def is_footer_displayed(self) -> bool:
        """
        Проверяет видимость футера страницы.

        Returns:
            bool
        """
        return self.check_if_element_visible(MainPageLocators.FOOTER)

    @allure.step(
            'Проверить отображение навигационной панели'
            ' при прокрутке страницы'
        )
    def is_navbar_fixed_after_scroll(self, delta_x=0, delta_y=1000) -> bool:
        """
        Проверяет фиксацию навигационной панели при скролле.

        Выполняет скролл страницы на `delta_y` пикселей и убеждается, что
        позиция навигационной панели не изменилась (панель зафиксирована).

        Args:
            delta_x (int, optional): Смещение по горизонтали.
            По умолчанию — 0.
            delta_y (int, optional): Смещение по вертикали.
            По умолчанию — 1000 px.

        Returns:
            bool
        """
        navbar = self.find_element(
            MainPageLocators.NAVIGATION_BAR
        )
        init_location = navbar.location

        action = ActionChains(self.driver)
        action.scroll_by_amount(delta_x, delta_y).perform()

        navbar_after = self.find_element(
            MainPageLocators.NAVIGATION_BAR
        )
        new_location = navbar_after.location

        return init_location['y'] == new_location['y']

    @allure.step('Проверить переход по меню навигации на другую страницу')
    def go_to_lifetime_membership(self) -> str:
        """
        Проверяет навигацию по сайту через меню в хедере.

        Выполняет следующие действия:
        1. Закрывает всплывающее окно (если есть).
        2. Кликает по пункту "Lifetime Membership" в навбаре.
        3. Проверяет, что открылся раздел "Lifetime Membership Club".

        Returns:
            str
        """
        self.close_popup()
        self.click_element(MainPageLocators.NAVBAR_LIFETIME_MEMBERSHIP)
        self.wait.until(EC.presence_of_all_elements_located(
            ((By.TAG_NAME, 'body'))
        ))
        page_title = self.find_element(
            LifetimeMembershipPageLocators.HEADING_TITLE
        )
        return page_title.text
