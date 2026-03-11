from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER = (
        By.CSS_SELECTOR,
        'div.ast-above-header-wrap'
    )
    HEADER_CONTACTS = (
        By.CSS_SELECTOR,
        'div.ast-above-header-wrap div ul li a[href]'
    )
    HEADER_SOCIAL_MEDIA = (
        By.CSS_SELECTOR,
        'div.header-social-inner-wrap a[href]'
    )
    NAVIGATION_BAR = (
        By.CSS_SELECTOR,
        '[class*=bar-wrap] [data-section="section-hb-menu-1"]'
    )
    NAVBAR_ALL_COURSES = (
        By.CSS_SELECTOR,
        '#menu-item-27580'
    )
    NAVBAR_LIFETIME_MEMBERSHIP = (
        By.CSS_SELECTOR,
        '#menu-item-27580 ul li:first-child a span.menu-text'
    )
    CLOSE_POPUP = (
        By.CSS_SELECTOR,
        'div i.eicon-close'
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
    FOOTER_ADDRESS = (
        By.XPATH,
        '//span[contains(text(), "Way2Automation")]'
    )
    FOOTER_PHONE_NUMBERS = (
        By.XPATH, (
            '//div[contains(@class, "elementor-element-695441a0")]'
            '//ul/li/a[starts-with(@href, "tel:")]'
        )
    )
    FOOTER_EMAILS = (
        By.XPATH, (
            '//div[contains(@class, "elementor-element-695441a0")]'
            '//ul/li/a[starts-with(@href, "mailto")]'
        )
    )
    ABOUT_US_BLOCK = (
        By.CSS_SELECTOR, (
            '[data-id="573bc308"]'
            ' div .elementor-element-695441a0 div ul li'
            ' span.elementor-icon-list-text'
        )
    )
    REGISTER_NOW_BUTTON = (
        By.XPATH,
        '//*[contains(text(), "Register Now")]'
    )
    MOST_POPULAR_COURSES = (
        By.CSS_SELECTOR,
        'div[class*=info-box-carousel] div.swiper-wrapper'
    )
    SLIDER_ARROW_PREV = (
        By.CSS_SELECTOR,
        '.elementor-swiper-button-prev'
    )
    SLIDER_ARROW_NEXT = (
        By.CSS_SELECTOR,
        'elementor-swiper-button-next'
    )


class LifetimeMembershipPageLocators:
    HEADING_TITLE = (
        By.XPATH,
        '//*[@id="post-25580"]/div//section/div//h1'
    )


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
