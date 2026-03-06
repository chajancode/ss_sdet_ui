import pytest

from pages.login_page import LoginPage


@pytest.mark.ui
class TestLoginPage:
    def test_login_page(
            self,
            login_page: LoginPage
    ) -> None:
        login_page.check_fields_visibility()
        login_page.check_login_button_is_not_clickable()
        login_page.check_fill_fields_and_login_success(
            username='angular', password='password'
        )
        login_page.check_logout()
        login_page.check_fill_fields_and_login_fail(
            username='ralugna', password='drowssap'
        )
