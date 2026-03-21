from typing import Callable

from selenium.webdriver import Chrome, Firefox, Edge, Safari
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver

from config.params import URL_GRID
from config.browser_options import (
    get_chrome_options,
    get_edge_options,
    get_safari_options,
    get_firefox_options
)

BROWSERS = ['chrome', 'edge', 'firefox', 'safari']

OPTIONS: dict[str, Callable] = {
    'chrome': get_chrome_options,
    'edge': get_edge_options,
    'firefox': get_firefox_options,
    'safari': get_safari_options
}

DRIVERS: dict[str, Callable[..., WebDriver]] = {
    'chrome': Chrome,
    'edge': Edge,
    'firefox': Firefox,
    'safari': Safari
}


class DriverFactory:

    @staticmethod
    def create_driver(browser: str, grid_mode: bool = False) -> WebDriver:

        if browser not in BROWSERS:
            raise ValueError('Браузер \'{browser}\' не поддерживается')

        options = OPTIONS[browser]()

        if grid_mode:
            driver = webdriver.Remote(
                command_executor=URL_GRID,
                options=options
            )

        driver = DRIVERS[browser](options=options)
        return driver
