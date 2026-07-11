from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (
        By.CSS_SELECTOR,
        '.site-header'
    )
    NAVIGATION_BAR = (
        By.CSS_SELECTOR,
        '.container.nav'
    )
    NAVBAR_LIFETIME_MEMBERSHIP = (
        By.CSS_SELECTOR,
        '#navLinks a[href*="lifetime-membership"]'
    )
    CLOSE_POPUP = (
        By.CSS_SELECTOR,
        '#flyerClose'
    )
    COURSES_LIST = (
        By.CSS_SELECTOR,
        '.grid.grid-3:has(article)'
    )
    FOOTER = (
        By.CSS_SELECTOR,
        '.site-footer'
    )
