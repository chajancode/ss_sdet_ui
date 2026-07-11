from selenium.webdriver.common.by import By


class ContactPageLocators:
    EMAIL = (
        By.XPATH,
        '//b[normalize-space()="Email"]/following-sibling::span'
    )
    WHATSAPP = (
        By.XPATH,
        '//b[contains(text(),"WhatsApp")]/following-sibling::span'
    )
