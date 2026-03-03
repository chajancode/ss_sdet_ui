from selenium.webdriver.common.by import By


class MainPageLocators():
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
