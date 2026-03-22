import pytest
import allure

from pages.droppable_page import DroppablePage


@pytest.fixture(scope='function')
def opened_droppable_page(request, opened_droppable_page: DroppablePage):
    opened_droppable_page.open()
    request.cls.droppable_page = opened_droppable_page
    yield opened_droppable_page


@allure.epic('Тестирование UI')
@allure.feature('Перенос элемента')
@pytest.mark.ui
class TestDroppablePage:
    @allure.title('Проверка возможности drag and drop')
    @allure.description(
        'Проверка доступности переноса одного элемента в другой'
    )
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.parametrize('msg', ['Dropped!'])
    def test_drag_and_drop(
                self, opened_droppable_page: DroppablePage, msg: str, driver
            ):
        opened_droppable_page.switch_to_frame()
        opened_droppable_page.drag_and_drop_element()
        opened_droppable_page.check_text(expected_text=msg)
