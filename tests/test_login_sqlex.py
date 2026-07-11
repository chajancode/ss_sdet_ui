import pytest
import allure

from pages.sqlex_page import SqlexPage
from test_data.login_test_data_model import SqlexLoginData
from test_data.login_test_data_sets import SQLEX_LOGIN_DATA


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
                open_page,
                test_data: SqlexLoginData,
            ) -> None:
        sqlex_page: SqlexPage = open_page(SqlexPage)
        assert sqlex_page.do_login(**test_data.to_dict())

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
                open_page,
                test_data: SqlexLoginData,
            ) -> None:
        sqlex_page: SqlexPage = open_page(SqlexPage)
        assert sqlex_page.do_login(**test_data.to_dict())
