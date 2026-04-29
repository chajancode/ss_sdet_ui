import pytest
import allure

from pages.sqlex_page import SqlexPage
from test_data.login_test_data_model import SqlexLoginData
from test_data.login_test_data_sets import SQLEX_LOGIN_DATA


@pytest.fixture(scope='function')
def opened_sqlex_page(request, opened_sqlex_page: SqlexPage):
    opened_sqlex_page.open()
    request.cls.login_page = opened_sqlex_page
    yield opened_sqlex_page


@allure.epic('Тестирование UI')
@allure.feature('Авторизация с куками')
@pytest.mark.ui
class TestSqlexLogin:

    @allure.title('Проверка авторизации')
    @allure.description(
        'Проверка авторизации на сайте с логином и паролем.'
        ' Если до этого момента не было входа в систему, либо'
        ' срок жизни предыдущей сессии истёк, происходит вход в систему'
        ' и данные пользовательской сессии сохраняются в файл.'
        )
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(
            'test_data', SQLEX_LOGIN_DATA
    )
    def test_login_first(
                self,
                opened_sqlex_page: SqlexPage,
                test_data: SqlexLoginData,
                driver
            ) -> None:

        assert opened_sqlex_page.do_login(**test_data.to_dict())

    @allure.title('Проверка авторизации через сессию')
    @allure.description(
        'Проверка повторного входа на сайт. Если есть файл с данными'
        ' пользовательской сессии из куков с актуальным сроком жизни сессии,'
        ' происходит авторизация через установку куков.'
        )
    @pytest.mark.parametrize(
            'test_data', SQLEX_LOGIN_DATA
    )
    def test_login_with_cookie(
                self,
                opened_sqlex_page: SqlexPage,
                test_data: SqlexLoginData,
                driver
            ) -> None:

        assert opened_sqlex_page.do_login(**test_data.to_dict())
