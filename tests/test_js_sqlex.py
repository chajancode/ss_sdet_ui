import pytest
import allure

from pages.sqlex_page import SqlexPage


@pytest.fixture(scope='function')
def opened_sqlex_page(request, opened_sqlex_page: SqlexPage):
    opened_sqlex_page.open()
    request.cls.login_page = opened_sqlex_page
    yield opened_sqlex_page


@allure.epic('Тестирование UI')
@allure.feature('Работа с JavaScriptExecutor')
@pytest.mark.ui
class TestSqlexJSExecutor:

    @allure.title('Убрать фокус с поля ввода.')
    @allure.description('Убирает фокус с поля ввода посредством JavaScript')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_unfocus_field(
                self, opened_sqlex_page: SqlexPage, driver
            ) -> None:
        result = opened_sqlex_page.unfocus_field()
        assert result[1], f'{result[0]}'

    @allure.title('Проверка присутствия скролла на странице')
    @allure.description('Проверяет наличие прокрутки страницы.')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_page_has_scroll(
                self, opened_sqlex_page: SqlexPage, driver
            ) -> None:
        assert opened_sqlex_page.page_has_scroll(), (
                'Нет прокрутки страницы'
            )
