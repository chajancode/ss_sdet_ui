import time
import json
from typing import Optional

from selenium.webdriver.remote.webdriver import WebDriver


class CookieTools():
    """
    Утилита для работы с куками.
    """

    @staticmethod
    def _is_session_active(
        filename: str,
        session_life_time: int = 24
    ) -> tuple[bool, Optional[str | None]]:
        """
        Проверяет активна ли сессия на данный момент.

        Args:
            filename (str): Имя файла, в который сохраняется кука.
            session_life_time (int): Время жизни сессии в минутах
                    (по умолчанию: 24 минуты).

        Returns:
            tuple[bool, Optional[dict | None]]: Кортеж со значением True и
                 идентификатором сессии, если сессия активна.
                 Иначе False и None.
        """
        try:
            with open(filename, 'r') as file:
                php_session = json.load(file)

                current_time = time.time()
                saved_at_time = php_session['saved_at']
                remaining_time = (current_time - saved_at_time) / 60

                if remaining_time < session_life_time:
                    return (
                        True,
                        php_session['phpsessid']
                    )
                return (
                    False, None
                )
        except FileNotFoundError:
            return (False, None)

    @staticmethod
    def save_cookies(driver: WebDriver, filename) -> None:
        """
        Сохраняет куку с пользовательской сессией в файл.

        Args:
            driver (WebDriver): Веб-драйвер.
            filename (str): Имя файла, в который сохраняется кука.

        Returns:
            None
        """
        cookies = driver.get_cookies()

        php_session: dict | None = next((
            cookie for cookie in cookies if cookie['name'] == 'PHPSESSID'
        ), None)

        session = {
            'phpsessid': php_session,
            'saved_at': time.time()
        }

        with open(filename, 'w') as file:
            json.dump(session, file)

    @staticmethod
    def set_cookie(
            driver: WebDriver, url_logged_in: str, filename: str
            ) -> bool:
        """
        Устанавливает куку с пользовательской сессией.
        Args:
            driver (WebDriver): Веб-драйвер.
            url_logged_in (str): Адрес главной страницы, если пользователь
                залогинен.

        Returns:
            bool
        """

        is_active, cookie = CookieTools._is_session_active(filename)

        if is_active:
            driver.get(url_logged_in)
            driver.delete_all_cookies()
            driver.add_cookie(cookie)

            return True

        return False
