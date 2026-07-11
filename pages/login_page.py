from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config.pages_urls import URL_LOGIN_PAGE
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Страница авторизации приложения.

    Предоставляет методы для взаимодействия с элементами формы входа:
    заполнения полей, выполнения логина и проверки результатов.
    """
    def __init__(self, driver):
        """
        Инициализирует страницу авторизации.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver
            для управления браузером.
        """
        super().__init__(driver)

    @allure.step('Открыть страницу авторизации')
    def open(self) -> None:
        """
        Открывает страницу авторизации.

        Returns:
            None
        """
        self.url = self.driver.get(URL_LOGIN_PAGE)

    @allure.step('Заполнить поля {locator} значением {value}.')
    def fill_text_form(self, locator: Tuple[By, str], value: str) -> None:
        """
        Заполняет текстовое поле указанным значением.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск элемента.
            value (str): Текст, который нужно ввести в поле.

        Returns:
            None
        """
        self.find_element(locator).send_keys(value)

    @allure.step(
            'Выполненить процесс аутентификации.'
            ' Имя пользователя: {username},'
            ' пароль: {password}'
    )
    def do_login(
            self,
            username: str,
            password: str,
            msg_locator: Tuple[By, str],
            ) -> WebElement:
        """
        Выполняет процесс авторизации с указанными данными.

        Args:
            username (str): Имя пользователя для авторизации.
            password (str): Пароль пользователя.
            msg_locator (Tuple[By, str]): Кортеж, определяющий поиск
                элемента с сообщением результата авторизации.

        Returns:
            WebElement: Элемент с сообщением результата.
        """
        self.fill_text_form(
            LoginPageLocators.FLD_USERNAME, username
        )
        self.fill_text_form(
            LoginPageLocators.FLD_PASSWORD, password
        )
        self.fill_text_form(
            LoginPageLocators.FLD_USERNAME_DESCRIPTION, username
        )
        self.click_element(
            LoginPageLocators.BTN_LOGIN
        )
        return self.find_element(msg_locator)

    @allure.step('Видно ли поле Username?')
    def is_username_field_visible(self) -> bool:
        """
        Видно ли поле Username?
        """
        return self.check_if_element_visible(LoginPageLocators.FLD_USERNAME)

    @allure.step('Видно ли поле Password?')
    def is_password_field_visible(self) -> bool:
        """
        идно ли поле Password?
        """
        return self.check_if_element_visible(LoginPageLocators.FLD_PASSWORD)

    @allure.step('Видно ли поле Username description?')
    def is_username_description_field_visible(self) -> bool:
        """
        Видно ли поле Username description?
        """
        return self.check_if_element_visible(
            LoginPageLocators.FLD_USERNAME_DESCRIPTION
        )

    @allure.step('Кликабельна ли кнопка Login?')
    def is_login_button_clickable(self) -> bool:
        """
        Кликабельна ли кнопка Login?
        """
        return self.is_clickable(LoginPageLocators.BTN_LOGIN)

    @allure.step('Нажать Logout')
    def click_logout(self) -> None:
        """
        Кликает Logout
        """
        self.click_element(LoginPageLocators.BTN_LOGOUT)

    @allure.step(
            '{step_name} Пользователь: {username}, пароль: {password}.'
    )
    def submit_login(
            self, username: str, password: str,
            test_type: str, step_name: str,  # noqa
    ) -> str:
        """
        Логинится и возвращает текст сообщения-результата.
        """
        match test_type:
            case 'success': msg_locator = LoginPageLocators.MSG_LOGGED_IN
            case 'fail': msg_locator = LoginPageLocators.MSG_AUTH_ERROR
            case _: raise ValueError(f'Неизвестный test_type: {test_type}')
        return self.do_login(username, password, msg_locator).text
