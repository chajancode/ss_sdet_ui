from typing import Callable, Optional

from selenium.webdriver import Chrome, Firefox, Edge
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

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
}  # type: ignore


class DriverFactory:
    """
    Фабрика для создания веб-драйверов.
    """
    @staticmethod
    def create_driver(
        browser: str,
        remote_url: Optional[str] = None
    ) -> WebDriver:
        """
        Метод для создания вебдрайвер с набором опций.

        Args:
            browser (str): Имя браузера.
            remote_url (str): Адрес грида (Selenoid или Selenium Grid ). \
                Если передан - подключается к браузеру на Гриде.
                Если не передан - запускается браузер без Грида.

        Returns:
            WebDriver: Настроенный драйвер браузера.

        Raises:
            ValueError: Если передан неизвестный браузер.
        """
        if browser not in BROWSERS:
            raise ValueError(f'Браузер \'{browser}\' не поддерживается')

        options = OPTIONS[browser]()

        if remote_url:
            return webdriver.Remote(
                command_executor=remote_url,
                options=options
            )  # type: ignore

        return DRIVERS[browser](options=options)
