import pytest
import allure

from pages.alert_page import AlertPage
from utils.string_builders import expected_alert_text


@allure.epic('Тестирование UI')
@allure.feature('Проверка работы алерта.')
@pytest.mark.ui
class TestAlertPage:

    @allure.title('Ввод текста в алерт.')
    @allure.description(
            'Вызывает алерт, после нажатия на кнопку'
            ' внутри айфрейма, вводит текст в алерт и проверяет'
            ' появление текста под кнопкой вызова алерта.'
        )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_press_input_alert(
                self, open_page
            ):
        alert_page: AlertPage = open_page(AlertPage)
        text = 'Selenium'

        alert_page.click_input_alert_tab()
        alert_page.click_inner_button()
        alert_page.enter_text_and_apply(text)

        result = alert_page.get_result_text()
        expected = expected_alert_text(text)

        assert result == expected, (
            f'Текст не совпал. Ожидалось: {expected}, получено: {result}'
        )
