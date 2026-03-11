import pytest

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.params import USER_AGENT


@pytest.fixture(scope='session')
def driver():
    chrome_options = Options()
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
def main_page(driver: WebDriver) -> MainPage:
    page = MainPage(driver)
    return page


@pytest.fixture()
def login_page(driver: WebDriver) -> LoginPage:
    page = LoginPage(driver)
    return page
