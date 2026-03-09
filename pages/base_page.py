from typing import Tuple

from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver: WebDriver, wait=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait)

    def _find_element(self, locator: Tuple[By, str]) -> WebElement | None:
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, WebDriverException):
            return None

    def _find_elements(
                self, locator: Tuple[By, str]
            ) -> list[WebElement] | None:
        try:
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
        except (TimeoutException, WebDriverException):
            return None

    def _is_clickable(self, locator: Tuple[By, str]) -> WebElement | None:
        try:
            return self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )
        except (TimeoutException, WebDriverException):
            return None

    def _click_element(self, locator: Tuple[By, str]) -> WebElement | None:
        element = self._is_clickable(locator)
        if element is None:
            return None
        try:
            element.click()
            return element
        except WebDriverException:
            return None

    def _check_if_element_visible(
            self,
            locator: Tuple[By, str]
            ) -> WebElement | None:
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
                )
        except (TimeoutException, WebDriverException):
            return None
