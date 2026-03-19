from selenium.webdriver.common.by import By


class SqlexLocators:
    FLD_LOGIN = (
        By.CSS_SELECTOR,
        'input[type="text"][name="login"]'
    )
    FLD_PASSWORD = (
        By.CSS_SELECTOR,
        'input[type="password"][name="psw"]'
    )
    BTN_LOGIN = (
        By.CSS_SELECTOR,
        'input[type="submit"][name="subm1"]'
    )
    USERNAME = (
        By.CSS_SELECTOR,
        'tbody tr td:last-child .none'
    )
