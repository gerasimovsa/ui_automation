import datetime

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

            short_month_date = input_data[4]
            short_month = ''.join(filter(str.isalpha, short_month_date))
            full_month = datetime.datetime.strptime(short_month, '%b').strftime('%B')
            full_month_date = short_month_date.replace(short_month, str(full_month).lower())
            input_data[4] = full_month_date

            assert table_data == input_data, 'Validating that submitted form corresponds to the table'
