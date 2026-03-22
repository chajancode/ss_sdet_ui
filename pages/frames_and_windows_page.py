import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Tuple
from selenium.webdriver.common.by import By

from config.pages_urls import URL_FRAMES_AND_WINDOWS
from pages.base_page import BasePage
from locators.frames_and_windows_page_locators import (
                            FramesAndWindowsPageLocators
                        )


class FramesAndWindowsPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Открыть страницу Frames And Windows')
    def open(self):
        """
        Открывает страницу Frames And Windows.
        """
        self.driver.get(URL_FRAMES_AND_WINDOWS)

    @allure.step('Переключиться на новую вкладку')
    def _switch_to_last_tab(self) -> str:
        """
        Переключается на последнюю открытую вкладку.

        Returns:
            str: Хэндл новой вкладки
        """

        self.wait.until(EC.number_of_windows_to_be(2))

        last_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(last_window_handle)

        return last_window_handle

    @allure.step('Переключить контекст на iframe')
    def switch_to_frame(self, locator: Tuple[By, str]) -> None:
        """
        Переключает контекст на iframe.

        Args:
            locator (Tuple[By, str]): Локатор iframe.
        """
        frame = self.find_element(locator)
        if frame is None:
            raise AssertionError(f'Frame не найден по локатору: {locator}')
        self.driver.switch_to.frame(frame)

    @allure.step('Переключиться на iframe на странице с вкладками')
    def switch_to_new_tab_frame(self) -> None:
        """
        Переключается на iframe на странице Frames And Windows.
        """

        self.switch_to_frame(
            FramesAndWindowsPageLocators.FRAME_FRMS_AND_WINDOWS
        )

    @allure.step('Открыть новую вкладку')
    def open_new_browser_tab(self) -> str:
        """
        Открывает новую вкладку и переключается на неё.

        Returns:
            str: Хэндл новой вкладки
        """
        self.switch_to_new_tab_frame()

        element = self.click_element(
            FramesAndWindowsPageLocators.NEW_BROWSER_TAB
        )
        if element is None:
            raise AssertionError(
                'Не удалось кликнуть по кнопке открытия новой вкладки'
            )
        new_tab_handle = self._switch_to_last_tab()

        return new_tab_handle

    @allure.step('Открыть новую вкладку из текущей (ссылка внутри iframe)')
    def open_new_tab_from_current_tab(self) -> str:
        """
        Открывает новую вкладку по ссылке на текущей странице.
        Используется для открытия третьей вкладки.

        Returns:
            str: Хэндл новой вкладки
        """

        element = self.click_element(
            FramesAndWindowsPageLocators.NEW_BROWSER_TAB
        )
        if element is None:
            raise AssertionError(
                'Не удалось кликнуть по ссылке для открытия новой вкладки'
            )

        self.wait.until(EC.number_of_windows_to_be(3))

        last_window_handle = self.driver.window_handles[-1]
        self.driver.switch_to.window(last_window_handle)

        return last_window_handle

    @allure.step('Проверить количество открытых вкладок')
    def check_tabs_amount(self) -> int:
        """
        Возвращает количество открытых вкладок.

        Returns:
            int: Количество открытых вкладок
        """
        amount = len(self.driver.window_handles)

        assert amount == 3, (
            f'Количество вкладок не равно 3. Открыто: {amount}'
        )
