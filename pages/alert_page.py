import allure
from selenium.webdriver.support import expected_conditions as EC

from config.pages_urls import URL_ALERT
from pages.base_page import BasePage
from locators.alerts_page_locators import AlertPageLocators
from utils.collocator import alert_text_collocator


class AlertPage(BasePage):
    """
    Класс для работы со страницей Alert.
    """
    def __init__(self, driver):
        """
        Инициализирует AlertPage с указанным драйвером.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver для управления
                браузером
        """
        super().__init__(driver)

    @allure.step('Открыть страницу Alert.')
    def open(self):
        """
        Открывает страницу Alert в браузере.

        """
        self.driver.get(URL_ALERT)

    @allure.step('Нажать Input Alert')
    def click_input_alert_tab(self):
        """
        Переключается на вкладку Input Alert.

        Returns:
            None
        """
        self.click_element(
            AlertPageLocators.TAB_INPUT_ALERT
        )

    @allure.step('Нажать кнопку внутри фрейма')
    def click_inner_button(self):
        """
        Нажимает кнопку внутри iframe.

        Переключает контекст драйвера на iframe и выполняет клик по кнопке.

        Returns:
            None

        Raises:
            AssertionError: Если не удалось нажать на кнопку внутри фрейма.
        """
        self.switch_to_frame(AlertPageLocators.IFRAME)

        assert self.click_element(
            AlertPageLocators.BTN_INSIDE_INPUT_ALERT
            ), 'Не удалось нажать на кнопку.'

    @allure.step('Ввести текст в появившийся алерт и подтвердить')
    def enter_text_and_apply(self, text: str = 'Selenium'):
        """
        Вводит указанный текст в alert и подтверждает ввод.

        Ожидает появления alert, вводит переданный текст, затем подтверждает
        действие. После подтверждения ожидает исчезновения alert.

        Args:
            text (str, optional): Текст для ввода в alert.
                По умолчанию 'Selenium'.

        Returns:
            None

        Raises:
            AssertionError: Если alert не появился в течение ожидаемого времени
        """
        alert = self.is_alert_present()
        alert.send_keys(text)
        alert.accept()
        self.wait.until_not(EC.alert_is_present())

    @allure.step('Проверить, что введённый текст появился.')
    def check_if_text_appeared(self, text: str = 'Selenium'):
        """
        Проверяет, что введённый текст отобразился на странице после
         подтверждения alert.

        Находит элемент с результатом и сравнивает его текст с ожидаемым.
        В случае несоответствия выбрасывает исключение AssertionError.

        Args:
            text (str, optional): Текст, который был введён в alert.
                По умолчанию 'Selenium'.

        Returns:
            None

        Raises:
            AssertionError: Если текст не появился или не соответствует
                ожидаемому значению.
        """
        result = self.find_element(AlertPageLocators.MSG_RESULT)
        expected = alert_text_collocator(text)
        assert result.text == expected, (
            f'Текст не появился, или не соответствует ожидаемому.'
            f' Ожидалось {expected}, получено {result.text}'
        )
