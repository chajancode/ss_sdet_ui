import re


class RegexpPatterns:

    PHONE_PATTERN = re.compile(
        r'^\+(\d{1,3})'
        r'[-.\s]?(\d{1,4})'
        r'[-.\s]?(\d{1,4})'
        r'[-.\s]?(\d{1,9})$'
    )
    SKYPE_PATTERN = re.compile(r'^skype:[^?]*\?chat$')
    EMAIL_PATTERN = re.compile(
        r'^mailto:[a-zA-Z0-9._%+-]+'
        r'@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    SOCIAL_MEDIA_PATTERN = re.compile(
        r'google\.com|linkedin\.com|facebook\.com|youtube\.com'
    )
