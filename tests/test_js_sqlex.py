import pytest
import allure

from pages.sqlex_page import SqlexPage


@allure.epic('Тестирование UI')
@allure.feature('Работа с JavaScriptExecutor')
@pytest.mark.ui
class TestSqlexJSExecutor:

    @allure.title('Убрать фокус с поля ввода.')
    @allure.description('Убирает фокус с поля ввода посредством JavaScript')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_unfocus_field(
                self, open_page
            ) -> None:
        sqlex_page: SqlexPage = open_page(SqlexPage)
        result = sqlex_page.unfocus_field()
        assert result[1], f'{result[0]}'  # type: ignore

    @allure.title('Проверка присутствия скролла на странице')
    @allure.description('Проверяет наличие прокрутки страницы.')
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_page_has_scroll(
                self, open_page
            ) -> None:
        sqlex_page: SqlexPage = open_page(SqlexPage)
        assert sqlex_page.page_has_scroll(), (
                'Нет прокрутки страницы'
            )
