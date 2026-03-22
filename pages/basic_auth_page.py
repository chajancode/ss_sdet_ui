import allure

from config.pages_urls import URL_BASIC_AUTH
from pages.base_page import BasePage
from locators.basic_auth_page_locators import BasicAuthPageLocators
from utils.collocator import basic_auth_collocator


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
        auth_url = basic_auth_collocator(username, password)
        self.driver.get(auth_url)
        self.click_display_image()

    @allure.step('Проверить появление изображения')
    def check_if_image_loaded(self):
        """
        Проверяет, что защищённое изображение успешно загрузилось после
        аутентификации.

        Ожидает появления изображения на странице.

        Returns:
            None

        Raises:
            AssertionError: Если изображение не появилось.
        """
        image = self.check_if_element_visible(
                BasicAuthPageLocators.DOWNLOADED_IMG
            )

        assert image, 'Изображение не появилось.'
