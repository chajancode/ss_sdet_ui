import allure
import pytest

from pages.contact_page import ContactPage
from utils.batch_assert import BatchAssert
from utils.string_checkers import StringChecker as SC


class TestContactPage:
    @allure.epic('Тестирование UI')
    @allure.feature('Страница контактов')
    @allure.title('Проверка контактов')
    @pytest.mark.ui
    def test_contact_page(self, open_page) -> None:
        contact_page: ContactPage = open_page(ContactPage)

        email = contact_page.get_email()
        whatsapp = contact_page.get_whatsapp()

        batch = BatchAssert()
        batch.check(
            bool(email) and SC.is_email(email.text),
            f'Нет имейла или он не соответствует формату: {email.text}'
        )
        batch.check(
            bool(whatsapp) and SC.is_phone_number(whatsapp.text),
            f'Нет ватсапа, либо не соответствует формату: {whatsapp.text}'
        )
        batch.report()
