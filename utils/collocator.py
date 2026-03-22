from config.pages_urls import URL_BASIC_AUTH


def alert_text_collocator(text: str) -> str:
    """
    Собирает ожидаемое сообщение.

    Args:
        text (str): Текст для вставки в сообщение.

    Returns:
        str: Сообщение с приветствием.
    """
    return f'Hello {text}! How are you today?'


def basic_auth_collocator(username: str, password: str) -> str:
    """
    Собирает url для basic auth.

    Args:
        username (str): Имя пользователя.
        password (str): Пароль.

    Returns:
        str: url для базовой аутентификации.
    """
    url = URL_BASIC_AUTH.split('://')
    return f'{url[0]}://{username}:{password}@{url[1]}'
