import allure

from selenium.webdriver.remote.webelement import WebElement

from config.pages_urls import URL_CONTACT_PAGE
from locators.contact_page_locators import ContactPageLocators
from pages.base_page import BasePage


class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open(self):
        self.driver.get(URL_CONTACT_PAGE)

    @allure.step('Получить email')
    def get_email(self) -> WebElement:
        return self.driver.find_element(*ContactPageLocators.EMAIL)

    @allure.step('Получить WhatsApp')
    def get_whatsapp(self) -> list[WebElement]:
        return self.driver.find_element(*ContactPageLocators.WHATSAPP)
