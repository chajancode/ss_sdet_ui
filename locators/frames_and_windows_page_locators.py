from selenium.webdriver.common.by import By


class FramesAndWindowsPageLocators:
    FRAME_FRMS_AND_WINDOWS = (
        By.CSS_SELECTOR,
        '#example-1-tab-1 > div > iframe'
    )
    NEW_BROWSER_TAB = (
        By.CSS_SELECTOR,
        'div p a[href="#"][target="_blank"]'
    )
