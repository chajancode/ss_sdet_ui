import pytest
import allure

from pages.basic_auth_page import BasicAuthPage


@pytest.fixture(scope='function')
def opened_auth_page(request, opened_auth_page: BasicAuthPage):
    opened_auth_page.open()
    request.cls.alert_page = opened_auth_page
    yield opened_auth_page


@allure.epic('Тестирование UI')
@allure.feature('Проверка Basic Authentication.')
@pytest.mark.ui
class TestFramesAndWindowsPage:

    @allure.title('Прохождение Basic Auth')
    @allure.description(
            'Проверяет прохождение базовой аутентификации.'
            ' Вызывает нативное окно браузера и обходит его,'
            ' отправляя реквизиты через адресную строку.'
        )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_press_input_alert(
                self, opened_auth_page: BasicAuthPage, driver
            ):
        opened_auth_page.click_display_image()
        opened_auth_page.authenticate()
        opened_auth_page.check_if_image_loaded()
