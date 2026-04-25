from typing import Callable

from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

from config.params import URL_GRID
from config.browser_options import (
    get_chrome_options,
    get_edge_options,
    get_firefox_options
)

BROWSERS = ['chrome', 'edge', 'firefox']

OPTIONS: dict[str, Callable] = {
    'chrome': get_chrome_options,
    'edge': get_edge_options,
    'firefox': get_firefox_options,
}

DRIVERS: dict[str, Callable[..., WebDriver]] = {
    'chrome': Chrome,
    'edge': Edge,
    'firefox': Firefox,
}


class DriverFactory:
    """
    Фабрика для создания веб-драйверов.
    """
    @staticmethod
    def create_driver(browser: str, grid_mode: bool = False) -> WebDriver:
        """
        Метод для создания вебдрайвер с набором опций.

        Args:
            browser (str): Название браузера.
            grid_mode (bool): Режим запуска тестов (локально или через
                Selenium Grid). По умолчанию - False.

        Returns:
            WebDriver: Настроенный драйвер браузера.

        Raises:
            ValueError: Если передан неизвестный браузер.
        """
        if browser not in BROWSERS:
            raise ValueError('Браузер \'{browser}\' не поддерживается')

        options = OPTIONS[browser]()

        if grid_mode:
            driver = webdriver.Remote(
                command_executor='http://selenoid:4444/wd/hub',
                options=options
            )
        else:
            driver = DRIVERS[browser](options=options)

        return driver
