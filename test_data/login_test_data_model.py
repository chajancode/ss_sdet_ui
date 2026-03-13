from dataclasses import dataclass, asdict


@dataclass
class LoginTestData:
    """
    Тестовые данные для авторизации.

    Attributes:
        username (str): Имя пользователя.
        password (str): Пароль (неверный).
        msg_expected (str): Ожидаемый текст сообщения
            об ошибке авторизации.
        test_type (str): Тип проверки ('success' или 'fail').
        step_name (str): Название шага для отчёта Allure.
    """
    username: str
    password: str
    msg_expected: str
    test_type: str
    step_name: str

    def to_dict(self):
        """
        Преобразует атрибуты в словарь.

        Returns:
            dict[str, Any]
        """
        return asdict(self)
