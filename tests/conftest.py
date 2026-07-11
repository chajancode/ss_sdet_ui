import pytest
import allure

from selenium.webdriver.remote.webdriver import WebDriver

from config.drivers import BROWSERS, DriverFactory
from config.settings import settings


def pytest_addoption(parser: pytest.Parser):
    parser.addoption(
        '--grid',
        action='store_true',
        help='Запуск тестов в Selenium Grid / Selenoid'
    )
    parser.addoption(
        '--browser',
        default='chrome',
        help=(
            'Имя браузера. По умолчанию \'chrome\'.'
            ' \'all\' запускает все браузеры.'
            'Перечисление через запятую, запускает перечисленные.'
            '(например: \'chrome,firefox\')'
        )
    )


def pytest_generate_tests(metafunc):
    if 'browser_name' in metafunc.fixturenames:
        browser = metafunc.config.getoption('--browser')

        if browser == 'all':
            browsers = BROWSERS
        else:
            browsers = browser.split(',')

        metafunc.parametrize('browser_name', browsers)


@pytest.fixture
def browser_name(request: pytest.FixtureRequest):
    if hasattr(request, 'param'):
        return request.param
    return request.config.getoption('--browser')


@pytest.fixture(scope='function')
def driver(request: pytest.FixtureRequest, browser_name: str):
    remote_url = settings.grid_url if \
        request.config.getoption('--grid') else None
    driver = None
    try:
        driver = DriverFactory.create_driver(browser_name, remote_url)
        yield driver
    finally:
        if driver:
            driver.quit()


@pytest.fixture
def open_page(driver: WebDriver):
    def open(page_class):
        page = page_class(driver)
        page.open()
        return page
    return open


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(
                item: pytest.Item,
            ):
    outcome = yield
    report: pytest.TestReport = outcome.get_result()

    if 'driver' in item.funcargs:  # type: ignore
        driver: WebDriver = item.funcargs['driver']  # type: ignore

        if report.when == 'call' and report.failed:
            screenshot = driver.get_screenshot_as_png()
            screenshot_name = f'Ошибка в тесте: {item.name}'
            allure.attach(
                screenshot,
                name=screenshot_name
            )
