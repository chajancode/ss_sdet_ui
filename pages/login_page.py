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

    def check_fields_visibility(self):
        assert self._check_if_element_visible(
            LoginPageLocators.FIELD_USERNAME
        ), 'Поле "Username" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FIELD_PASSWORD
        ), 'Поле "Password" не отображается'
        assert self._check_if_element_visible(
            LoginPageLocators.FIELD_USERNAME_DESCRIPTION
        ), 'Поле "Username (username description)" не отображается'

    def check_login_button_is_not_clickable(self):
        assert not self._click_element(
            LoginPageLocators.BUTTON_LOGIN
        )

    def check_fill_fields_and_login_success(
            self,
            username: str = 'angular',
            password: str = 'password'
            ) -> None:
        self._fill_text_form(
            LoginPageLocators.FIELD_USERNAME, username
        )
        self._fill_text_form(
            LoginPageLocators.FIELD_PASSWORD, password
        )
        self._fill_text_form(
            LoginPageLocators.FIELD_USERNAME_DESCRIPTION, username
        )
        self._click_element(
            LoginPageLocators.BUTTON_LOGIN
        )
        msg = self._find_element(LoginPageLocators.MSG_LOGGED_IN)

        assert msg.text == 'You\'re logged in!!', (
            f'Сообщение не появилось или появился другой текст. '
            f'Получен текст: {msg.text}'
        )
