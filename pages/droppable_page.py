import allure
from selenium.webdriver.common.action_chains import ActionChains


from config.params import URL_DROPPABLE
from pages.base_page import BasePage
from locators.droppable_page_locators import DroppablePageLocators


class DroppablePage(BasePage):
    def __init__(self, driver):
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
    def switch_to_frame(self):
        frame = self.find_element(DroppablePageLocators.FRAME_DROPPABLE)
        self.driver.switch_to.frame(frame)

    @allure.step('Перетащить элемент в принимающий')
    def drag_and_drop_element(self):
        to_be_dragged = self.find_element(
            DroppablePageLocators.ELMNT_TO_BE_DRAGGED
        )
        where_to_drag = self.find_element(
            DroppablePageLocators.ELMNT_WHERE_TO_DRAG
        )
        self.action.drag_and_drop(to_be_dragged, where_to_drag).perform()

    @allure.step('Проверить изменился ли текст в принимающем элементе')
    def check_text(self, expected_text: str):
        current_text = self.find_element(
                DroppablePageLocators.ELMNT_WHERE_TO_DRAG
            ).text
        assert current_text == expected_text, (
                f'Элемент не удалось переместить или текст не соответствует'
                f' ожидаемому. Получен текст: {current_text},'
                f' ожидался {expected_text}'
            )
