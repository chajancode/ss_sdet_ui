from config.params import URL_LOGIN_PAGE
from locators.locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = driver.get(URL_LOGIN_PAGE)

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
