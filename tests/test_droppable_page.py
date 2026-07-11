import pytest
import allure

from pages.droppable_page import DroppablePage


@allure.epic('Тестирование UI')
@allure.feature('Перенос элемента')
@pytest.mark.ui
class TestDroppablePage:
    @allure.title('Проверка возможности drag and drop')
    @allure.description(
        'Проверка доступности переноса одного элемента в другой'
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('expected_text', ['Dropped!'])
    def test_drag_and_drop(
                self, open_page, expected_text: str
            ):
        droppable_page: DroppablePage = open_page(DroppablePage)
        droppable_page.switch_to_droppable_frame()
        droppable_page.drag_and_drop_element()
        text = droppable_page.get_dropped_text()

        assert text == expected_text, (
                f'Элемент не удалось переместить или текст не соответствует'
                f' ожидаемому. Получен текст: {text},'
                f' ожидался {expected_text}'
            )
