from selenium.webdriver.common.by import By


class LoginPageLocators:
    FLD_USERNAME = (
        By.CSS_SELECTOR,
        'input#username'
    )
    FLD_PASSWORD = (
        By.CSS_SELECTOR,
        'input#password'
    )
    FLD_USERNAME_DESCRIPTION = (
        By.XPATH, (
            '//*[contains(@id, "_input_username_0")]'
            '[contains(@name, "_input_username_0")]'
        )
    )
    BTN_LOGIN = (
        By.CSS_SELECTOR,
        'button.btn-danger'
    )
    BTN_LOGOUT = (
        By.CSS_SELECTOR,
        'div a[href="#/login"]'
    )
    MSG_LOGGED_IN = (
        By.XPATH,
        "//p[contains(text(), \"You're logged in\")]"
    )
    MSG_AUTH_ERROR = (
        By.CSS_SELECTOR,
        'div [ng-if="Auth.error"]'
    )
