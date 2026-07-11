import allure

from pages.main_page import MainPage
from utils.batch_assert import BatchAssert


@allure.epic('Тестирование UI')
@allure.feature('Главная страница')
class TestMainPage:
    @allure.title('Проверка открытия главной страницы')
    @allure.description(
        'Проверка отображения всех элементов главной страницы'
    )
    @allure.severity(allure.severity_level.CRITICAL)
    def test_main_page_elements(
                self, open_page
            ) -> None:
        main_page: MainPage = open_page(MainPage)

        batch = BatchAssert()
        batch.check(main_page.is_header_displayed(), 'Хэдер не отображается')
        batch.check(main_page.is_navbar_displayed(), 'Навбар не отображается')
        batch.check(main_page.is_courses_displayed(), 'Курсы не отображаются')
        batch.check(main_page.is_footer_displayed(), 'Футер не отображается')
        batch.report()

    @allure.title('Проверка меню навигации при скроллинге страницы')
    @allure.description(
        'Проверка отображения меню навигации при скроллинге страницы вниз'
    )
    @allure.severity(allure.severity_level.NORMAL)
    def test_navbar_on_scroll(
                self, open_page
            ) -> None:
        main_page: MainPage = open_page(MainPage)
        assert main_page.is_navbar_fixed_after_scroll(), (
            'Навигация не зафиксирована при скролле'
        )

    @allure.title(
            'Проверка перехода на другие страницы через меню навигации'
    )
    @allure.description(
        'Проверка перехода на другую страницу, используя меню навигации'
    )
    @allure.severity(allure.severity_level.BLOCKER)
    def test_transition_through_navbar(
                self, open_page
            ) -> None:
        main_page: MainPage = open_page(MainPage)

        title = main_page.go_to_lifetime_membership()
        batch = BatchAssert()
        batch.check(
            'lifetime-membership-club' in main_page.current_url,
            f'Неверный URL: {main_page.current_url}'
        )
        batch.check(
            'The Lifetime Membership Club' in title,
            f'Неверный заголовок: {title}'
        )
        batch.report()
