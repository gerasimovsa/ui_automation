import pytest
import allure
from pom.forms_page import PracticeFormPage


@pytest.mark.usefixtures('setup')
@allure.suite("Forms Page")
class TestFormsPage:
    @allure.feature("Practice Forms")
    class TestPracticeForms:
        @allure.title("Forms test")
        def test_form(self):
            practice_form_page = PracticeFormPage(self.driver)
            practice_form_page.open_page()
            input_data = practice_form_page.submit_filled_form()
            table_data = practice_form_page.get_table_data()
            assert table_data == input_data, 'Validating that submitted form corresponds to the table'
