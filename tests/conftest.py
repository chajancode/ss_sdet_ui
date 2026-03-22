import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver

from config.drivers import BROWSERS, DriverFactory
from pages.alert_page import AlertPage
from pages.basic_auth_page import BasicAuthPage
from pages.droppable_page import DroppablePage
from pages.frames_and_windows_page import FramesAndWindowsPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.sqlex_page import SqlexPage


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--grid',
        action='store_true',
        help='Запуск тестов в Selenium Grid'
    )
    parser.addoption(
        '--browser',
        default='chrome',
        help=(
            'Имя браузера. По умолчанию \'chrome\'.'
            ' \'all\' запускает все браузеры.'
        )
    )


def pytest_generate_tests(metafunc):
    if 'browser_name' in metafunc.fixturenames:
        browser = metafunc.config.getoption('--browser')

        if browser == 'all':
            browsers = BROWSERS
            metafunc.parametrize('browser_name', browsers)
        else:
            metafunc.parametrize('browser_name', [browser])


@pytest.fixture
def browser_name(request: pytest.FixtureRequest):
    if hasattr(request, 'param'):
        return request.param
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def driver(request: pytest.FixtureRequest, browser_name: str):
    grid_mode = request.config.getoption('--grid')
    driver = None
    try:
        driver = DriverFactory.create_driver(browser_name, grid_mode)
        yield driver
    finally:
        if driver:
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


@pytest.fixture()
def opened_droppable_page(driver: WebDriver) -> DroppablePage:
    page = DroppablePage(driver)
    return page


@pytest.fixture()
def opened_windows_page(driver: WebDriver) -> FramesAndWindowsPage:
    page = FramesAndWindowsPage(driver)
    return page


@pytest.fixture()
def opened_alert_page(driver: WebDriver) -> AlertPage:
    page = AlertPage(driver)
    return page


@pytest.fixture()
def opened_auth_page(driver: WebDriver) -> BasicAuthPage:
    page = BasicAuthPage(driver)
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
