from typing import Tuple
from abc import ABC, abstractmethod

import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.common import (
    NoSuchElementException,
    TimeoutException
)
from selenium.webdriver.support import expected_conditions as EC


class BasePage(ABC):
    """
    Абстрактный базовый класс для всех страниц, подлежащих автоматизированному
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

    @abstractmethod
    def open(self) -> None:
        """
        Абстрактный метод открытия страницы.

        Raises:
            NotImplementedError: если метод не реализован в дочернем класс
        """

    @allure.step('Найти элемент: {locator}.')
    def find_element(self, locator: Tuple[By, str]) -> WebElement:
        """
        Находит первый элемент, соответствующий локатору, с ожиданием его
        присутствия.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
               и локатор элемента (например, `(By.ID, "my_id")`).

        Returns:
            WebElement: Найденный элемент.
        """
        return self.wait.until(
            EC.presence_of_element_located(locator),
            message=f'Элемент "{locator}" не найден'  # type: ignore
        )

    @allure.step('Найти все элементы: {locator}.')
    def find_elements(
                self, locator: Tuple[By, str]
            ) -> list[WebElement]:
        """
        Находит все элементы, соответствующие локатору, с ожиданием их
        присутствия.

        Ожидает появления всех элементов на странице.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск, и локатор
                    элементов (например, `(By.CLASS_NAME, "my_class")`).

        Returns:
            list[WebElement]: Список найденных элементов.
        """
        return self.wait.until(
            EC.presence_of_all_elements_located(locator),
            message=f'Элементы "{locator}" не найдены'  # type: ignore
        )

    @allure.step('Проверить кликабельность элемента: {locator}')
    def is_clickable(self, locator: Tuple[By, str]) -> bool:
        """
        Проверяет, доступен ли элемент для клика, с ожиданием.

        Ожидает, пока элемент станет кликабельным (видимым и активным).
        Если элемент не становится кликабельным в течение заданного таймаута,
        возвращает False.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                и локатор элемента.

        Returns:
            bool
        """
        try:
            self.wait.until(
                EC.element_to_be_clickable(locator)  # type: ignore
            )
            return True
        except TimeoutException:
            return False

    @allure.step('Кликнуть по элементу: {locator}.')
    def click_element(self, locator: Tuple[By, str]) -> WebElement:
        """
        Кликает по элементу, если он доступен для клика.

        Сначала проверяет, что элемент кликабелен. Если да, выполняет клик.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                    и локатор элемента.

        Returns:
            WebElement: Элемент, по которому был выполнен клик.
        """
        element = self.wait.until(
            EC.element_to_be_clickable(locator),  # type: ignore
            message=f'Элемент не кликабелен: {locator}',
        )
        element.click()
        return element

    @allure.step('Проверить видимость элемента: {locator}.')
    def check_if_element_visible(
            self,
            locator: Tuple[By, str]
            ) -> bool:
        """
        Проверяет видимость элемента с ожиданием.

        Ожидает, пока элемент станет видимым на странице. Если элемент не
        становится видимым в течение заданного таймаута, возвращает `None`.

        Args:
            locator (Tuple[By, str]): Кортеж, определяющий поиск,
                и локатор элемента.

        Returns:
            bool.
        """
        try:
            self.wait.until(
                EC.visibility_of_element_located(locator)  # type: ignore
                )
            return True
        except TimeoutException:
            return False

    @allure.step('Переключить контекст на iframe.')
    def switch_to_frame(self, locator: tuple[By, str]):
        """
        Переключает контекст на iframe.

        Args:
            locator (tuple[By, str]): Локатор iframe.
        Returns:
            None
        """
        try:
            frame = self.find_element(locator)
            self.driver.switch_to.frame(frame)
        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(
                f'Не удалось переключиться на iframe: {e}'
            ) from e

    @allure.step('Проверить появление алерта.')
    def is_alert_present(self) -> Alert:
        """
        Проверяет появление алерта.

        Returns:
            alert (Alert): Экземпляр класса Alert.

        Raises:
            AssertionError: Если алерт не появился.
        """
        try:
            alert = self.wait.until(EC.alert_is_present())
        except (TimeoutException, NoSuchElementException) as e:
            raise AssertionError(
                f'Алерт не появился: {e} '
            ) from e
        return alert
