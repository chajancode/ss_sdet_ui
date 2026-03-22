import os

from dotenv import load_dotenv


load_dotenv()

FILE_SQLX_COOKIES = 'cookies_sqlex.json'

URL_GRID = os.getenv('GRID_URL')

USER_AGENT = (
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'
    ' AppleWebKit/537.36 (KHTML, like Gecko)'
    ' Chrome/122.0.0.0 Safari/537.36)'
)
