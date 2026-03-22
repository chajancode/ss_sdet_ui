from selenium.webdriver.common.by import By


class AlertPageLocators:

    TAB_INPUT_ALERT = (
        By.XPATH,
        '//*[@href="#example-1-tab-2"][@target="_self"]'
    )
    BTN_INSIDE_INPUT_ALERT = (
        By.XPATH,
        '//button[contains(@onclick, "myFunction")]'
    )
    IFRAME = (
        By.CSS_SELECTOR,
        'iframe[src*="alert/input-alert.html"]'
    )
    MSG_RESULT = (By.ID, "demo")
