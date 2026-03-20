import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from config.browser_options import get_chrome_options
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.params import URL_GRID
from pages.sqlex_page import SqlexPage


@pytest.fixture
def selenium_grid_url(scope='session'):
    return URL_GRID


@pytest.fixture(scope='function')
def driver(selenium_grid_url):
    chrome_options = get_chrome_options()
    driver = webdriver.Remote(
        command_executor=selenium_grid_url,
        options=chrome_options
    )
    yield driver
    driver.quit()


@pytest.fixture()
def opened_main_page(driver: WebDriver) -> MainPage:
    page = MainPage(driver)
    return page


@pytest.fixture()
def opened_login_page(driver: WebDriver) -> LoginPage:
    page = LoginPage(driver)
    return page


@pytest.fixture()
def opened_sqlex_page(driver: WebDriver) -> SqlexPage:
    page = SqlexPage(driver)
    return page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(
                item: pytest.Item,
                call: pytest.CallInfo
            ):
    outcome = yield
    report: pytest.TestReport = outcome.get_result()

    if "driver" in item.funcargs:
        driver: WebDriver = item.funcargs['driver']

        if report.when == 'call' and report.failed:
            screenshot = driver.get_screenshot_as_png()
            screenshot_name = f'Ошибка в тесте: {item.name}'
            allure.attach(
                screenshot,
                name=screenshot_name
            )
