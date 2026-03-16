from test_data.login_test_data_model import LoginTestData


VALID_LOGIN_DATA = LoginTestData(
    username='angular',
    password='password',
    msg_expected='You\'re logged in!!',
    test_type='success',
    step_name='Проверить вход в систему с валидными данными.'
)
INVALID_LOGIN_DATA = LoginTestData(
    username='ralugna',
    password='drowssap',
    msg_expected='Username or password is incorrect',
    test_type='fail',
    step_name='Проверить вход в систему с невалидными данными.'
)


def collect_datasets() -> list[LoginTestData]:
    """
    Собирает тестовые данные в список для передачи в фикстуру.

    Returns:
        list(LoginTestData): Cписок тестовых данных.
    """

    return [VALID_LOGIN_DATA, INVALID_LOGIN_DATA]
