import pytest
import allure

from pages.alert_page import AlertPage


@pytest.fixture(scope='function')
def opened_alert_page(request, opened_alert_page: AlertPage):
    opened_alert_page.open()
    request.cls.alert_page = opened_alert_page
    yield opened_alert_page


@allure.epic('Тестирование UI')
@allure.feature('Проверка работы алерта.')
@pytest.mark.ui
class TestFramesAndWindowsPage:

    @allure.title('Ввод текста в алерт.')
    @allure.description(
            'Вызывает алерт, после нажатия на кнопку'
            ' внутри айфрейма, вводит текст в алерт и проверяет'
            ' появление текста под кнопкой вызова алерта.'
        )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_press_input_alert(
                self, opened_alert_page: AlertPage, driver
            ):
        opened_alert_page.click_input_alert_tab()
        opened_alert_page.click_inner_button()
        opened_alert_page.enter_text_and_apply()
        opened_alert_page.check_if_text_appeared()
