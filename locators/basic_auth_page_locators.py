from selenium.webdriver.common.by import By


class BasicAuthPageLocators:

    BTN_DISPLAY_IMAGE = (
        By.XPATH,
        "//input[@value='Display Image']"
    )
    DOWNLOADED_IMG = (
        By.ID,
        'downloadImg'
    )
