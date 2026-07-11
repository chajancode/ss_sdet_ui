import allure

from config.pages_urls import URL_BASIC_AUTH
from pages.base_page import BasePage
from locators.basic_auth_page_locators import BasicAuthPageLocators
from utils.string_builders import basic_auth_url_builder


class BasicAuthPage(BasePage):
    """
    Класс для работы со страницей Basic Authentication.
    """
    def __init__(self, driver):
        """
        Инициализирует BasicAuthPage с указанным драйвером.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver для управления
                браузером
        """
        super().__init__(driver)

    @allure.step('Открыть страницу Basic Authentication.')
    def open(self):
        """
        Открывает страницу Basic Authentication в браузере.

        """
        self.driver.get(URL_BASIC_AUTH)

    @allure.step('Нажать на кнопку Display Image')
    def click_display_image(self):
        """
        Выполняет клик по кнопке Display Image.

        Returns:
            None

        Raises:
            AssertionError: Если кнопка не кликабельна или не найдена.
        """

        self.click_element(BasicAuthPageLocators.BTN_DISPLAY_IMAGE)

    @allure.step('Пройти аутентификацию с заданными реквизитами.')
    def authenticate(
                self, username: str = 'httpwatch', password: str = 'httpwatch'
            ):
        """
        Выполняет базовую аутентификацию с указанными учётными данными.

        Формирует URL с встроенными учётными данными (username:password@host)
        и выполняет навигацию по этому URL. После успешной аутентификации
        автоматически нажимает кнопку Display Image для загрузки защищённого
        контента.

        Args:
            username (str, optional): Имя пользователя для аутентификации.
                По умолчанию 'httpwatch'.
            password (str, optional): Пароль для аутентификации.
                По умолчанию 'httpwatch'.

        Returns:
            None

        Raises:
            AssertionError: Если изображение не появилось.
        """
        auth_url = basic_auth_url_builder(username, password)
        self.driver.get(auth_url)
        self.click_display_image()

    @allure.step('Проверить появление изображения')
    def is_image_loaded(self) -> bool:
        """
        Возвращает результат проверки появления изображения.

        Returns:
            bool
        """
        return self.check_if_element_visible(
                BasicAuthPageLocators.DOWNLOADED_IMG
            )
