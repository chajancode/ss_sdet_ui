from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.safari.options import Options as SafariOptions


from config.params import USER_AGENT


def get_chrome_options() -> ChromeOptions:
    """
    Создаёт и настраивает Options для браузера Chrome.

    Returns:
        ChromeOptions
    """
    options = ChromeOptions()

    prefs = {
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument(f'user-agent={USER_AGENT}')
    options.add_argument('--start-maximized')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-notifications')
    options.page_load_strategy = 'eager'

    return options


def get_firefox_options() -> FirefoxOptions:
    """
    Создаёт и настраивает Options для браузера Edge.

    Returns:
        FirefoxOptions
    """
    options = FirefoxOptions()

    return options


def get_edge_options() -> EdgeOptions:
    """
    Создаёт и настраивает Options для браузера Edge.

    Returns:
        EdgeOptions
    """
    options = EdgeOptions()

    return options


def get_safari_options() -> SafariOptions:
    """
    Создаёт и настраивает Options для браузера Safari.

    Returns:
        SafariOptions
    """
    options = SafariOptions()

    return options
