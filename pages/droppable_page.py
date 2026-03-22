import allure
from selenium.webdriver.common.action_chains import ActionChains


from config.pages_urls import URL_DROPPABLE
from pages.base_page import BasePage
from locators.droppable_page_locators import DroppablePageLocators


class DroppablePage(BasePage):
    """
    Страница для упражнения на перетаскивание элементов.
    """
    def __init__(self, driver):
        """
        Инициализирует страницу авторизации.

        Args:
            driver (WebDriver): Экземпляр класса WebDriver
            для управления браузером.
            action (ActionChains): Экземпляр класса ActionCahins
            для выполнения действий на странице.
        """
        super().__init__(driver)
        self.action = ActionChains(self.driver)

    @allure.step('Открыть страницу Droppable')
    def open(self):
        """
        Открывает страницу Droppable.

        Returns:
            None
        """
        self.driver.get(URL_DROPPABLE)

    @allure.step('Переключиться на iframe')
    def switch_to_droppable_frame(self):
        """
        Переключает контекст на iframe, содержащий элементы для drag and drop.

        Returns:
            None
        """
        self.switch_to_frame(DroppablePageLocators.FRAME_DROPPABLE)

    @allure.step('Перетащить элемент в принимающий')
    def drag_and_drop_element(self):
        """
        Выполняет операцию drag and drop (перетаскивание) элемента.

        Returns:
            None
        """
        to_be_dragged = self.find_element(
            DroppablePageLocators.ELMNT_TO_BE_DRAGGED
        )
        where_to_drag = self.find_element(
            DroppablePageLocators.ELMNT_WHERE_TO_DRAG
        )
        self.action.drag_and_drop(to_be_dragged, where_to_drag).perform()

    @allure.step('Проверить изменился ли текст в принимающем элементе')
    def check_text(self, expected_text: str):
        """
        Проверяет, изменился ли текст в принимающем элементе
        после drag and drop.

        Метод получает текущий текст из целевого элемента и сравнивает его
        с ожидаемым значением.

        Args:
            expected_text (str): Ожидаемый текст, который должен появиться
                в принимающем элементе после перетаскивания.

        Returns:
            None

        Raises:
            AssertionError: Если текст в элементе не соответствует ожидаемому
        """
        current_text = self.find_element(
                DroppablePageLocators.ELMNT_WHERE_TO_DRAG
            ).text
        assert current_text == expected_text, (
                f'Элемент не удалось переместить или текст не соответствует'
                f' ожидаемому. Получен текст: {current_text},'
                f' ожидался {expected_text}'
            )
