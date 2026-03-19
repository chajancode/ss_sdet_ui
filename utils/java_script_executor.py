from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver

from utils.js_scripts import HAS_VERTICAL_SCROLL_SCRIPT, UNFOCUS_ELEMENT_SCRIPT


def unfocus_element(driver: WebDriver, argument: str) -> tuple[str | bool]:
    """
    Убирает фокус с элемента DOM.

    Args:
        driver (WebDriver): Веб-драйвер.
        argument (str): CSS локатор.

    Returns:
        tuple[str | bool]: Информация об элементе и статусе выполненной
            проверки (True - фокус убран,
            False - фокус не убран/не найден элемент.)
    """
    result = driver.execute_script(UNFOCUS_ELEMENT_SCRIPT, argument)
    return tuple(result)


def has_scroll(driver: WebDriver) -> Any:
    """
    Проверяет присутствие вертикального скролла на странице.

    Args:
        driver (WebDriver): Веб-драйвер.

    Returns:
        Any
    """
    result = driver.execute_script(HAS_VERTICAL_SCROLL_SCRIPT)
    return result
