import allure
from selenium.common import TimeoutException, NoSuchElementException

from config.pages_urls import URL_SQLEX_INDEX, URL_SQLEX_PAGE
from pages.base_page import BasePage
from utils.cookie_tools import CookieTools
from locators.sqlex_page_locators import SqlexLocators
from config.params import FILE_SQLX_COOKIES
from utils.java_script_executor import has_scroll, unfocus_element


class SqlexPage(BasePage):
    def __init__(self, driver, wait=20) -> None:
        """
        Инициализирует главную страницу.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver для
            управления браузером

        Returns:
            None
        """
        super().__init__(driver, wait)

    @allure.step('Открыть страницу')
    def open(self) -> None:
        """
        Открывает сраницу Sql-ex.ru

        Returns:
            None
        """
        self.driver.get(URL_SQLEX_PAGE)

    @allure.step('Попробовать залогиниться через куки.')
    def _login_with_cookies(self, expected_username: str) -> bool:
        """
        Логинится через куки, если пользовательская сессия активна.

        Args:
            expected_username (str): Ожидаемый логин на странице, с
                авторизованным пользователем.

        Returns:
            bool
        """
        try:
            with allure.step('Проверить наличие активной сессии.'):
                cookie = CookieTools.set_cookie(
                    self.driver, URL_SQLEX_INDEX, FILE_SQLX_COOKIES
                )
            if cookie:
                with allure.step('Обновить страницу с установленной кукой.'):
                    self.driver.refresh()
                is_logged_in = self.find_element(SqlexLocators.USERNAME)
                if is_logged_in.text == expected_username:
                    allure.step('Войти через куку.')
                    return True
        except (TimeoutException, NoSuchElementException):
            return False
        return False

    @allure.step('Авторизоваться на сайте.')
    def do_login(
                self, expected_nickname: str, login: str, password: str
            ) -> bool:
        """
        Проверяет авторизацию на сайте. Если пользовательская сессия активна,
        авторизуется через куки, если нет - авторизуется по логину и паролю
        и обновляет куку в файле.

        Args:
            expected_nickname (str): Ожидаемый ник пользователя на сайте.
            login (str): Логин.
            password (str): Пароль.

        Returns:
            bool
        """

        if self._login_with_cookies(expected_nickname):
            return True

        try:
            self.find_element(SqlexLocators.FLD_LOGIN).send_keys(login)
            self.find_element(SqlexLocators.FLD_PASSWORD).send_keys(password)
            self.click_element(SqlexLocators.BTN_LOGIN)

            is_logged_in = self.check_if_element_visible(
                SqlexLocators.USERNAME
            )
            if is_logged_in.text == expected_nickname:
                with allure.step('Сохранить данные сессии.'):
                    CookieTools.save_cookies(self.driver, FILE_SQLX_COOKIES)
                    return True
        except (TimeoutException, NoSuchElementException):
            return False
        return False

    @allure.step('Убрать фокус из поля ввода.')
    def unfocus_field(self) -> tuple[str | bool]:
        """
        Убирает фокус с поля ввода логина.
        """
        locator = SqlexLocators.FLD_LOGIN

        if self.find_element(locator):

            result = unfocus_element(self.driver, locator)

            allure.attach(
                f'Результат: {result}',
                attachment_type=allure.attachment_type.TEXT
            )
            return result
        return 'Поле логина не найдено', False

    @allure.step('Определить наличие скролла на странице')
    def page_has_scroll(self) -> None:
        """
        Определяет наличие скролла на странице.
        """
        result = has_scroll(self.driver)

        allure.attach(
            f'Результат: {result}',
            attachment_type=allure.attachment_type.TEXT
        )
        return result
