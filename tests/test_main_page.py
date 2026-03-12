import pytest
import allure

from pages.main_page import MainPage


@pytest.fixture(scope='class')
def opened_main_page(request, opened_main_page: MainPage):
    opened_main_page.open()
    request.cls.login_page = opened_main_page
    yield opened_main_page


@allure.epic('Тестирование UI')
@allure.feature('Главная страница')
class TestMainPage:
    @allure.title('Проверка открытия главной страницы')
    @allure.description(
        'Проверка отображения всех элементов главной страницы'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_main_page_elements(self, opened_main_page: MainPage) -> None:
        opened_main_page.check_header_is_displayed()
        opened_main_page.check_navbar_is_displayed()
        opened_main_page.check_courses_is_displayed()
        opened_main_page.check_footer_is_displayed()

    @allure.title('Проверка контактной информации в хедере')
    @allure.description(
        'Проверка отображения номеров телефонов, ссылку на Skype, email'
        ' и ссылки на соцсети.'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_check_header_contacts(self, opened_main_page: MainPage) -> None:
        opened_main_page.check_contacts()
        opened_main_page.check_social_media()

    @allure.title('Проверка контактной информации и адреса в футере')
    @allure.description(
        'Проверка отображения адреса, номеров телефонов, адресов email'
        ' в футере.'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_check_footer_contacts(self, opened_main_page: MainPage) -> None:
        opened_main_page.check_footer_address()
        opened_main_page.check_footer_phone_numbers()
        opened_main_page.check_footer_emails()

    @allure.title('Проверка меню навигации при скроллинге страницы')
    @allure.description(
        'Проверка отображения меню навигации при скроллинге страницы вниз'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_navbar_on_scroll(self, opened_main_page: MainPage) -> None:
        opened_main_page.check_navbar_on_scroll()

    @allure.title(
            'Проверка перехода на другие страницы через меню навигации'
    )
    @allure.description(
        'Проверка перехода на другую страницу, используя меню навигации'
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_transition_through_navbar(
            self, opened_main_page: MainPage
            ) -> None:
        opened_main_page.check_navigation_through_navbar()
