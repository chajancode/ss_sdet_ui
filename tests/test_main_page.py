import pytest

from pages.main_page import MainPage


@pytest.mark.ui
class TestMainPage:
    def test_main_page(
            self,
            main_page: MainPage
    ) -> None:
        main_page.check_header_is_displayed()
        main_page.check_navbar_is_displayed()
        main_page.check_courses_is_displayed()
        main_page.check_footer_is_displayed()
