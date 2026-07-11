import pytest
import allure

from pages.frames_and_windows_page import FramesAndWindowsPage


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
                self, open_page
            ):
        windows_page: FramesAndWindowsPage = open_page(FramesAndWindowsPage)
        windows_page.open_new_browser_tab()
        windows_page.open_new_tab_from_current_tab()
        amount = windows_page.get_tabs_amount()
        assert amount == 3, (
            f'Количество вкладок не равно 3. Открыто: {amount}'
        )
