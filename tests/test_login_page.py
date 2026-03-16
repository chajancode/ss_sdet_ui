import pytest
import allure

from pages.login_page import LoginPage
from test_data.login_test_data_model import LoginTestData
from test_data.login_test_data_sets import collect_datasets


@pytest.fixture(scope='function')
def opened_login_page(request, opened_login_page: LoginPage):
    opened_login_page.open()
    request.cls.login_page = opened_login_page
    yield opened_login_page


@allure.epic('Тестирование UI')
@allure.feature('Страница авторизации')
@pytest.mark.ui
class TestLoginPage:
    @allure.title('Проверка полей ввода')
    @allure.description(
        'Проверка отображения полей "username", "password".'
        '  Кнопка "login" неактивна при незаполненных полях'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_authentication_fields(self, opened_login_page: LoginPage) -> None:
        opened_login_page.check_fields_visibility()
        opened_login_page.check_login_button_is_not_clickable()

    @allure.title('Проверка авторизации')
    @allure.description('Проверка авторизации с различными наборами данных')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'test_data', collect_datasets()
    )
    def test_login(
                self,
                opened_login_page: LoginPage,
                test_data: LoginTestData
            ) -> None:
        opened_login_page.check_login(**test_data.to_dict())

        if test_data.test_type == 'success':
            opened_login_page.check_logout()
