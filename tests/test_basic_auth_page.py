import pytest
import allure

from pages.basic_auth_page import BasicAuthPage


@allure.epic('Тестирование UI')
@allure.feature('Проверка Basic Authentication.')
@pytest.mark.ui
class TestBasicAuthPage:

    @allure.title('Прохождение Basic Auth')
    @allure.description(
            'Проверяет прохождение базовой аутентификации.'
            ' Вызывает нативное окно браузера и обходит его'
            ' отправкой реквизитов через адресную строку.'
        )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_basic_auth(
                self, open_page
            ):
        auth_page: BasicAuthPage = open_page(BasicAuthPage)
        auth_page.click_display_image()
        auth_page.authenticate()
        result = auth_page.is_image_loaded()
        assert result, 'Изображение не появилось'
