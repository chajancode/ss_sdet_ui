from typing import Tuple

import allure
from selenium.webdriver.chrome .webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common import TimeoutException, WebDriverException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для всех страниц, подлежащих автоматизированному
    тестированию веб-приложений.

    Предоставляет интерфейс для взаимодействия с элементами страницы
    через Selenium WebDriver с использованием явных ожиданий.

    Атрибуты:
        driver (WebDriver): Экземпляр класса WebDriver для управления
                                браузером
        wait (WebDriverWait): Объект явного ожидания с таймаутом
    """
    def __init__(self, driver: WebDriver, wait=20):
        """
        Инициализирует BasePage с указанным драйвером и временем ожидания

        Args:
            driver (WebDriver): Экземпляр класса WebDriver для управления
                                   браузером
            wait (int, optional): Таймаут ожидания в секундах (
                                    по умолчанию 20 секунд)
        """

        self.driver = driver
        self.wait = WebDriverWait(self.driver, wait)

    @allure.step('Найти элемент: {locator}.')
    def find_element(self, locator: Tuple[By, str]) -> WebElement | None:
        """
        Находит первый элемент, соответствующий локатору, с ожиданием его
        присутствия. Если элемент не найден в течение заданного таймаута,
        возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
               и локатор элемента (например, `(By.ID, "my_id")`).

        Returns:
            WebElement | None: Найденный элемент или `None`, если элемент
                не найден.

        Returns:
            None
        """
        try:
            return self.wait.until(
                EC.presence_of_element_located(locator)
            )
        except (TimeoutException, WebDriverException):
            return None

    @allure.step('Найти все элементы: {locator}.')
    def find_elements(
                self, locator: Tuple[By, str]
            ) -> list[WebElement] | None:
        """
        Находит все элементы, соответствующие локатору, с ожиданием их
        присутствия.

        Ожидает появления всех элементов на странице. Если элементы не найдены
        в течение заданного таймаута, возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск, и локатор 
                    элементов (например, `(By.CLASS_NAME, "my_class")`).

        Returns:
            list[WebElement] | None: Список найденных элементов или `None`,
                если элементы не найдены.
        """
        try:
            return self.wait.until(
                EC.presence_of_all_elements_located(locator)
            )
        except (TimeoutException, WebDriverException):
            return None

    @allure.step('Проверить кликабельность элемента: {locator}')
    def is_clickable(self, locator: Tuple[By, str]) -> WebElement | None:
        """
        Проверяет, доступен ли элемент для клика, с ожиданием.

        Ожидает, пока элемент станет кликабельным (видимым и активным).
        Если элемент не становится кликабельным в течение заданного таймаута,
        возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                и локатор элемента.

        Returns:
            WebElement | None: Кликабельный элемент или `None`, если
                условие не выполнено.
        """
        try:
            return self.wait.until(
                EC.element_to_be_clickable(
                    locator
                )
            )
        except (TimeoutException, WebDriverException):
            return None

    @allure.step('Кликнуть по элементу: {locator}.')
    def click_element(self, locator: Tuple[By, str]) -> WebElement | None:
        """
        Кликает по элементу, если он доступен для клика.

        Сначала проверяет, что элемент кликабелен. Если да, выполняет клик.
        В случае ошибки при клике или если элемент не кликабелен,
        возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                    и локатор элемента.

        Returns:
            WebElement | None`: Элемент, по которому был выполнен клик, или
            `None` в случае ошибки или недоступности элемента.
        """
        element = self.is_clickable(locator)
        if element is None:
            return None
        try:
            element.click()
            return element
        except WebDriverException:
            return None

    @allure.step('Проверить видимость элемента: {locator}.')
    def check_if_element_visible(
            self,
            locator: Tuple[By, str]
            ) -> WebElement | None:
        """
        Проверяет видимость элемента с ожиданием.

        Ожидает, пока элемент станет видимым на странице. Если элемент не
        становится видимым в течение заданного таймаута, возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                и локатор элемента.

        Returns:
            WebElement | None: Видимый элемент или `None`, если элемент не
                виден или не найден.
        """
        try:
            return self.wait.until(
                EC.visibility_of_element_located(locator)
                )
        except (TimeoutException, WebDriverException):
            return None
