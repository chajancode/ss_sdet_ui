import re


class RegexpPatterns:
    """
    Коллекция регулярных выражений для валидации различных типов данных.

    Содержит скомпилированные шаблоны для проверки:
    - номеров телефонов;
    - ссылок Skype;
    - email-адресов и ссылок mailto;
    - URL социальных сетей.
    """
    PHONE_PATTERN = re.compile(
        r'^\+(\d{1,3})'
        r'[\s.-]*'
        r'(\d{4,5})'
        r'[\s.-]+'
        r'(\d{2,3})'
        r'[\s.-]+'
        r'(\d{3,4})$'
    )
    SKYPE_PATTERN = re.compile(r'^skype:[^?]*\?chat$')
    EMAIL_LINK_PATTERN = re.compile(
        r'^mailto:[a-zA-Z0-9._%+-]+'
        r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    EMAIL_PATTERN = re.compile(
        r'^[a-zA-Z0-9._-]'
        r'+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,4}$'
    )
    SOCIAL_MEDIA_PATTERN = re.compile(
        r'.*(google\.com|linkedin\.com|facebook\.com|youtube\.com).*'
    )
