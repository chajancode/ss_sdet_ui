from selenium.webdriver.common.by import By


class MainPageLocators():
    HEADER = (
        By.CSS_SELECTOR,
        'div.ast-above-header-wrap'
    )
    NAVIGATION_BAR = (
        By.CSS_SELECTOR,
        '[class*=bar-wrap] [data-section="section-hb-menu-1"]'
    )
    COURSES_LIST = (
        By.CSS_SELECTOR, (
            '[class*="elementor-element-5b4952c1"]'
            ' [class*=elementor-container]'
            ' .elementor-icon-box-title'
        )
    )
    FOOTER = (
        By.CSS_SELECTOR,
        '[data-id="573bc308"]'
    )
    REGISTER_NOW_BUTTON = (
        By.XPATH,
        '//*[contains(text(), "Register Now")]'
    )
