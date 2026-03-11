from utils.regexp_patterns import RegexpPatterns as RP


class StringChecker:
    """
    Вспомогательный класс для проверки строк по регулярным выражениям.

    Предоставляет статические методы для валидации различных форматов
    данных:
    номеров телефонов, ссылок Skype, email-адресов и ссылок, URL соцсетей.
    """
    @staticmethod
    def _string_check(string: str, pattern: str) -> bool:
        return bool(pattern.match(string.strip()))

    @staticmethod
    def is_phone_number(string: str) -> bool:
        return StringChecker._string_check(string, RP.PHONE_PATTERN)

    @staticmethod
    def is_skype(string: str) -> bool:
        return StringChecker._string_check(string, RP.SKYPE_PATTERN)

    @staticmethod
    def is_email_link(string: str) -> bool:
        return StringChecker._string_check(string, RP.EMAIL_LINK_PATTERN)

    @staticmethod
    def is_email(string: str) -> bool:
        return StringChecker._string_check(string, RP.EMAIL_PATTERN)

    @staticmethod
    def is_social_media(string: str) -> bool:
        return StringChecker._string_check(string, RP.SOCIAL_MEDIA_PATTERN)
