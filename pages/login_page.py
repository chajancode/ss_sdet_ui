from typing import Tuple

from selenium.webdriver.common.by import By

from config.params import URL_LOGIN_PAGE
from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = driver.get(URL_LOGIN_PAGE)

    def _fill_text_form(self, locator: Tuple[By, str], value: str):
        self._find_element(locator).send_keys(value)

    def _do_login(
            self,
            username: str,
            password: str,
            msg_expected: str,
            msg_locator: Tuple[By, str],
            ) -> None:
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
        msg = self._find_element(msg_locator)

        assert msg.text == msg_expected, (
            f'Сообщение не появилось или не соответствует ожидаемому. '
            f'Получен текст: {msg.text}, ожидалось: {msg_expected}'
        )

    def check_fields_visibility(self):
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_USERNAME
        ), 'Поле "Username" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_PASSWORD
        ), 'Поле "Password" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FLD_USERNAME_DESCRIPTION
        ), 'Поле "Username (username description)" не отображается'

    def check_login_button_is_not_clickable(self):
        assert not self._click_element(
            LoginPageLocators.BTN_LOGIN
        ), 'Кнопка "Login" кликабельна'

    def check_fill_fields_and_login_success(
            self,
            username: str,
            password: str
            ) -> None:
        self._do_login(
            username=username,
            password=password,
            msg_expected='You\'re logged in!!',
            msg_locator=LoginPageLocators.MSG_LOGGED_IN
        )

    def check_fill_fields_and_login_fail(
            self,
            username: str,
            password: str
            ) -> None:
        self._do_login(
            username=username,
            password=password,
            msg_expected='Username or password is incorrect',
            msg_locator=LoginPageLocators.MSG_AUTH_ERROR
        )

    def check_logout(self) -> None:
        self._click_element(
            LoginPageLocators.BTN_LOGOUT
        )
        self.check_fields_visibility()
        self.check_login_button_is_not_clickable()
