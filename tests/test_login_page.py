import pytest
import allure

from pages.login_page import LoginPage


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

    # @allure.title('Проверка успешной авторизации')
    # @allure.description(
    #     'Проверка авторизации с валидными "username" и "password".'
    # )
    # @allure.severity(allure.severity_level.BLOCKER)
    # def test_succesful_login(self, opened_login_page: LoginPage) -> None:
    #     opened_login_page.check_fill_fields_and_login_success(
    #         username='angular', password='password'
    #     )

    # @allure.title('Проверка успешного разлогирования')
    # @allure.description('Проверка успешного выхода из системы')
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_successful_logout(self, opened_login_page: LoginPage) -> None:
    #     opened_login_page.check_logout()

    # @allure.title('Проверка неуспешной авторизации')
    # @allure.description(
    #     'Проверка авторизации с невалидными "username" и "password".'
    # )
    # @allure.severity(allure.severity_level.CRITICAL)
    # def test_failed_login(self, opened_login_page: LoginPage) -> None:
    #     opened_login_page.check_fill_fields_and_login_fail(
    #         username='ralugna', password='drowssap'
    #     )

    @allure.title('Проверка авторизации')
    @allure.description('Проверка авторизации с различными наборами данных')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'username, password, msg_expected, test_type, step_name', [
            (
                'angular',
                'password',
                'You\'re logged in!!',
                'success',
                'Проверить вход в систему с валидными данными.'
            ),
            (
                'ralugna',
                'drowssap',
                'Username or password is incorrect',
                'fail',
                'Проверить вход в систему с невалидными данными.'
            )
        ]
    )
    def test_login(
                self,
                opened_login_page: LoginPage,
                username: str,
                password: str,
                msg_expected: str,
                test_type: str,
                step_name: str
            ) -> None:
        opened_login_page.check_login(
            username=username,
            password=password,
            msg_expected=msg_expected,
            test_type=test_type,
            step_name=step_name
        )
        if test_type == 'success':
            opened_login_page.check_logout()
