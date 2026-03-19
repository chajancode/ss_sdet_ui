from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver


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
    result = driver.execute_script(
        """
        var element = document.querySelector(arguments[0]);
        if (!element) {
            return ['Элемент не найден.', false];
        }
        if (element === document.activeElement) {
            element.blur();
            return ['Убран фокус с элемента.', true];
        } else {
            return ['Нет фокуса на элементе.'];
        }
        """,
        argument
    )
    return tuple(result)


def has_scroll(driver: WebDriver) -> Any:
    """
    Проверяет присутствие вертикального скролла на странице.

    Args:
        driver (WebDriver): Веб-драйвер.

    Returns:
        Any
    """
    result = driver.execute_script(
        """
         return document.documentElement.scrollHeight >
                document.documentElement.clientHeight;
        """
    )
    return result
