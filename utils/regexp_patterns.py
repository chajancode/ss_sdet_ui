import re


class RegexpPatterns:

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
