import pytest
import allure

from pages.login_page import LoginPage


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
    def test_authentication_fields(self, login_page: LoginPage) -> None:
        login_page.check_fields_visibility()
        login_page.check_login_button_is_not_clickable()

    @allure.title('Проверка успешной авторизации')
    @allure.description(
        'Проверка авторизации с валидными "username" и "password".'
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_succesful_login(self, login_page: LoginPage) -> None:
        login_page.check_fill_fields_and_login_success(
            username='angular', password='password'
        )

    @allure.title('Проверка успешного разлогирования')
    @allure.description('Проверка успешного выхода из системы')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_logout(self, login_page: LoginPage) -> None:
        login_page.check_logout()

    @allure.title('Проверка неуспешной авторизации')
    @allure.description(
        'Проверка авторизации с невалидными "username" и "password".'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_failed_login(self, login_page: LoginPage) -> None:
        login_page.check_fill_fields_and_login_fail(
            username='ralugna', password='drowssap'
        )
