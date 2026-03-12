class BatchAssert:
    """
    Утилита для пакетной проверки.
    Накапливает ошибки и выбрасывает исключение
    с информацией по каждой из них.
    """
    def __init__(self):
        self._errors: list = []

    def check(
            self, condition: bool, message: str
            ) -> None:
        """
        Проверяет условие на истинность и добавляет сообщение об ошибке
         в список, если условие ложно.

        Args:
            conditon (bool): Условие, которое должно быть проверено.
            message (str): Сообщение, которое должно передаваться, при
                        непрохождении проверки.

        Returns:
            None
        """
        if condition is None:
            self._errors.append(message)

    def report(self) -> None:
        """
        Выбрасывает исключение с информацией об ошибках,
         если есть невыполненные условия

        Raises:
            AssertionError
        """
        if self._errors:
            raise AssertionError(
                f'Обнаружены ошибки: {", ".join(self._errors)}'
            )
