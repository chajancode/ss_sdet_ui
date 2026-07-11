import pytest
import allure

from pages.login_page import LoginPage
from test_data.login_test_data_model import LoginTestData
from test_data.login_test_data_sets import collect_datasets
from utils.batch_assert import BatchAssert


def assert_login_form_is_ready(login_page: LoginPage) -> None:
    """
    Форма входа видна и кнопка Login неактивна при пустых полях
    """
    batch = BatchAssert()
    batch.check(login_page.is_username_field_visible(),
                'Поле "Username" не отображается')
    batch.check(login_page.is_password_field_visible(),
                'Поле "Password" не отображается')
    batch.check(login_page.is_username_description_field_visible(),
                'Поле "Username description" не отображается')
    batch.check(not login_page.is_login_button_clickable(),
                'Кнопка "Login" кликабельна')
    batch.report()


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
    def test_authentication_fields(
                self, open_page
            ) -> None:
        login_page: LoginPage = open_page(LoginPage)
        assert_login_form_is_ready(login_page)

    @allure.title('Проверка авторизации')
    @allure.description('Проверка авторизации с различными наборами данных')
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
        'test_data', collect_datasets()
    )
    def test_login(
                self,
                open_page,
                test_data: LoginTestData,
            ) -> None:
        login_page: LoginPage = open_page(LoginPage)
        message = login_page.submit_login(
            username=test_data.username,
            password=test_data.password,
            test_type=test_data.test_type,
            step_name=test_data.step_name
        )
        assert message == test_data.msg_expected, (
            f'Сообщение не совпало. Получено: {message},'
            f' ожидалось: {test_data.msg_expected}'
        )
        if test_data.test_type == 'success':
            login_page.click_logout()
            assert_login_form_is_ready(login_page)
