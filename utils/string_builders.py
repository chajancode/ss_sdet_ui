from config.pages_urls import URL_BASIC_AUTH


def expected_alert_text(text: str) -> str:
    return f'Hello {text}! How are you today?'


def basic_auth_url_builder(username: str, password: str) -> str:
    url = URL_BASIC_AUTH.split('://')
    return f'{url[0]}://{username}:{password}@{url[1]}'
