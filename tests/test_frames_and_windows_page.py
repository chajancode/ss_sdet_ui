import pytest
import allure

from pages.frames_and_windows_page import FramesAndWindowsPage


@pytest.fixture(scope='function')
def opened_windows_page(request, opened_windows_page: FramesAndWindowsPage):
    opened_windows_page.open()
    request.cls.windows_page = opened_windows_page
    yield opened_windows_page


@allure.epic('Тестирование UI')
@allure.feature('Открывание новых окон')
@pytest.mark.ui
class TestBasicAuthPage:

    @allure.title('Открывание новых окон и переход на них')
    @allure.description(
            'Проверка открытия новых окон/вкладок и перехода на них'
        )
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_browser_tabs(
                self, opened_windows_page: FramesAndWindowsPage, driver
            ):
        opened_windows_page.open_new_browser_tab()
        opened_windows_page.open_new_tab_from_current_tab()
        opened_windows_page.check_tabs_amount()
