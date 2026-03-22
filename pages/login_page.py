from typing import Tuple

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config.params import URL_LOGIN_PAGE
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage
from utils.batch_assert import BatchAssert


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
            ) -> WebElement | None:
        """
        Выполняет процесс авторизации с указанными данными.

        Args:
            username (str): Имя пользователя для авторизации.
            password (str): Пароль пользователя.
            msg_locator (Tuple[By, str]): Кортеж, определяющий поиск
                элемента с сообщением результата авторизации.

        Returns:
            WebElement | None: Элемент с сообщением результата или `None`,
                если элемент не найден.

        Returns:
            None
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

    @allure.step('Проверить видимость обязательных полей формы авторизации')
    def check_fields_visibility(self) -> None:
        """
        Проверяет видимость обязательных полей формы авторизации.

        Убеждается, что поля "Username", "Password" и "Username description"
        отображаются на странице.

        Raises:
            AssertionError: Если какое‑либо из полей не отображается.

        Returns:
            None
        """
        batch_assert = BatchAssert()
        batch_assert.check(self.check_if_element_visible(
                    LoginPageLocators.FLD_USERNAME),
                    'Поле "Username" не отображается'
        )
        batch_assert.check(self.check_if_element_visible(
                    LoginPageLocators.FLD_PASSWORD),
                    'Поле "Password" не отображается'
        )
        batch_assert.check(self.check_if_element_visible(
                    LoginPageLocators.FLD_USERNAME_DESCRIPTION),
                    'Поле "Username (username description)" не отображается'
        )
        batch_assert.report()

    @allure.step('Проверить некликабельность кнопки "login".')
    def check_login_button_is_not_clickable(self) -> None:
        """
        Проверяет, что кнопка "Login" недоступна для клика.

        Raises:
            AssertionError: Если кнопка кликабельна.

        Returns:
            None
        """
        assert not self.click_element(
                LoginPageLocators.BTN_LOGIN
        ), 'Кнопка "Login" кликабельна'

    @allure.step('Проверить успешный выход из системы')
    def check_logout(self) -> None:
        """
        Проверяет процесс выхода из системы.

        Кликает по кнопке "Logout", затем проверяет, что:
        - форма входа снова видна;
        - кнопка "Login" неактивна при пустых полях.

        Raises:
            AssertionError: Если кнопка «Logout» не найдена или не
            кликабельна, либо если последующие проверки не пройдены.

        Returns:
            None
        """
        logout_btn = self.click_element(
                LoginPageLocators.BTN_LOGOUT
            )
        if not logout_btn:
            raise AssertionError(
                'Кнопка Logout не появилась или не кликабельна'
            )
        self.check_fields_visibility()
        self.check_login_button_is_not_clickable()

    @allure.step(
            '{step_name}'
            ' Имя пользователя: {username}, пароль: {password}.'
            ' Ожидаемое сообщение: {msg_expected}.'
    )
    def check_login(
            self,
            username: str,
            password: str,
            msg_expected: str,
            test_type: str,
            step_name: str # noqa
            ) -> None:
        """
        Проверяет вход в систему с различными наборами тестовых данных
        (валидными и невалидными)

        Args:
            username (str): Имя пользователя.
            password (str): Пароль (неверный).
            msg_expected (str): Ожидаемый текст сообщения
                об ошибке авторизации.
            test_type (str): Тип проверки ('success' или 'fail').
            step_name (str): Название шага для отчёта Allure.

        Raises:
            AssertionError: Если сообщение отсутствует или не соответствует
                ожидаемому результату.

        Returns:
            None
        """
        match test_type:
            case 'success': msg_locator = LoginPageLocators.MSG_LOGGED_IN
            case 'fail': msg_locator = LoginPageLocators.MSG_AUTH_ERROR

        msg = self.do_login(
            username=username,
            password=password,
            msg_locator=msg_locator
        )
        if msg:
            assert msg.text == msg_expected, (
                f'Сообщение не появилось или не соответствует ожидаемому. '
                f'Получен текст: {msg.text}, ожидалось: {msg_expected}'
            )
        else:
            raise AssertionError('Не соответствует ожидаемому результату.')
