import pytest
import allure

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.params import USER_AGENT


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
    prefs = {
        "profile.password_manager_leak_detection": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument(f'user-agent={USER_AGENT}')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-notifications')
    chrome_options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=chrome_options)
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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(
                item: pytest.Item,
                call: pytest.CallInfo
            ):
    outcome = yield
    report: pytest.TestReport = outcome.get_result()
    driver: WebDriver = item.funcargs['driver']

    if report.when == 'call' and report.failed:
        screenshot = driver.get_screenshot_as_png()
        screenshot_name = f'Ошибка в тесте: {item.name}'
        allure.attach(
            screenshot,
            name=screenshot_name
        )
