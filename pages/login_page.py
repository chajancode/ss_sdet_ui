from typing import Tuple

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from config.params import URL_LOGIN_PAGE
from locators.locators import LoginPageLocators
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

        **Args:**
            - `driver`: Экземпляр класса WebDriver для управления браузером.
        """
        super().__init__(driver)
        self.url = driver.get(URL_LOGIN_PAGE)

    def fill_text_form(self, locator: Tuple[By, str], value: str) -> None:
        """
        Заполняет текстовое поле указанным значением.

        Находит элемент по локатору и вводит заданный текст.

        **Args:**
            - `locator (Tuple[By, str])`: Кортеж, определяющий поиск элемента.
            - `value (str)`: Текст, который нужно ввести в поле.
        """
        self._find_element(locator).send_keys(value)

    def do_login(
            self,
            username: str,
            password: str,
            msg_locator: Tuple[By, str],
            ) -> WebElement | None:
        """
        Выполняет процесс авторизации с указанными данными.

        Заполняет поля логина и пароля, отправляет форму и возвращает
        элемент с сообщением результата.

        **Args:**
            - `username (str)`: Имя пользователя для авторизации.
            - `password (str)`: Пароль пользователя.
            - `msg_locator (Tuple[By, str])`: Кортеж, определяющий поиск
                элемента с сообщением результата авторизации.

        **Returns:**
            - `WebElement | None`: Элемент с сообщением результата или `None`,
                если элемент не найден.
        """
        self._fill_text_form(
            LoginPageLocators.FLD_USERNAME, username
        )
        self._fill_text_form(
            LoginPageLocators.FLD_PASSWORD, password
        )
        self._fill_text_form(
            LoginPageLocators.FLD_USERNAME_DESCRIPTION, username
        )
        self._click_element(
            LoginPageLocators.BTN_LOGIN
        )
        return self._find_element(msg_locator)

    def check_fields_visibility(self) -> None:
        """
        Проверяет видимость обязательных полей формы авторизации.

        Убеждается, что поля «Username», «Password» и «Username description»
        отображаются на странице.

        **Raises:**
            - `AssertionError`: Если какое‑либо из полей не отображается.
        """
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_USERNAME
        ), 'Поле "Username" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_PASSWORD
        ), 'Поле "Password" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_USERNAME_DESCRIPTION
        ), 'Поле "Username (username description)" не отображается'

    def check_login_button_is_not_clickable(self) -> None:
        """
        Проверяет, что кнопка «Login» недоступна для клика.

        Убеждается, что кнопка не активна (например, при незаполненных полях).

        **Raises:**
            - `AssertionError`: Если кнопка кликабельна.
        """
        assert not self._click_element(
                LoginPageLocators.BTN_LOGIN
        ), 'Кнопка "Login" кликабельна'

    def check_fill_fields_and_login_success(
            self,
            username: str,
            password: str,
            msg_expected='You\'re logged in!!'
            ) -> None:
        """Проверяет успешный вход в систему.

        Заполняет поля, выполняет логин и убеждается, что появилось
        ожидаемое сообщение об успешном входе.

        **Args:**
            - `username (str)`: Имя пользователя.
            - `password (str)`: Пароль.
            - `msg_expected (str, optional)`: Ожидаемый текст сообщения
                об успешном входе. По умолчанию — «You're logged in!!».

        **Raises:**
            - `AssertionError`: Если сообщение отсутствует или не соответствует
                ожидаемому результату.
        """
        msg = self.do_login(
            username=username,
            password=password,
            msg_locator=LoginPageLocators.MSG_LOGGED_IN
        )
        if msg:
            assert msg.text == msg_expected, (
                f'Сообщение не появилось или не соответствует ожидаемому. '
                f'Получен текст: {msg.text}, ожидалось: {msg_expected}'
            )
        else:
            raise AssertionError('Не соответствует ожидаемому результату')

    def check_fill_fields_and_login_fail(
            self,
            username: str,
            password: str,
            msg_expected='Username or password is incorrect',
            ) -> None:
        """
        Проверяет вход в систему с невалидными аргументами имени
        пользователя и пароля.

        Заполняет поля неверными данными, выполняет логин и убеждается,
        что появилось сообщение об ошибке.

        **Args:**
            - `username (str)`: Имя пользователя.
            - `password (str)`: Пароль (неверный).
            - `msg_expected (str, optional)`: Ожидаемый текст сообщения
                об ошибке авторизации. По умолчанию —
                «Username or password is incorrect».

        **Raises:**
            - `AssertionError`: Если сообщение отсутствует или не соответствует
                ожидаемому результату.
        """
        msg = self.do_login(
            username=username,
            password=password,
            msg_locator=LoginPageLocators.MSG_AUTH_ERROR
        )
        if msg:
            assert msg.text == msg_expected, (
                f'Сообщение не появилось или не соответствует ожидаемому. '
                f'Получен текст: {msg.text}, ожидалось: {msg_expected}'
            )
        else:
            raise AssertionError('Не соответствует ожидаемому результату')

    def check_logout(self) -> None:
        """
        Проверяет процесс выхода из системы.

        Кликает по кнопке «Logout», затем проверяет, что:
        - форма входа снова видна;
        - кнопка «Login» неактивна при пустых полях.

        **Raises:**
            - `AssertionError`: Если кнопка «Logout» не найдена или не
            кликабельна, либо если последующие проверки не пройдены.
        """
        logout_btn = self._click_element(
                LoginPageLocators.BTN_LOGOUT
            )
        if not logout_btn:
            raise AssertionError(
                'Кнопка Logout не появилась или не кликабельна'
            )
        self.check_fields_visibility()
        self.check_login_button_is_not_clickable()
