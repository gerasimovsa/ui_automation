import random
import time

import pytest
from pom.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablesPage


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestElementsPage:
    # def test_text_box(self):
    #     text_box_page = TextBoxPage(self.driver)
    #     expected_output_forms_text = text_box_page.fill_all_fields()
    #     output_forms_text = text_box_page.get_output_forms_text()
    #     assert expected_output_forms_text == output_forms_text, 'Validating Elements page forms output text'

    # def test_checkbox(self):
    #     checkbox = CheckBoxPage(self.driver)
    #     checkbox.expand_checkbox_list()
    #     checkbox.click_random_checkboxes()
    #     input_checkboxes = checkbox.get_checked_checkboxes_text()
    #     output_checkboxes = checkbox.get_output_results_text()
    #     print(input_checkboxes)
    #     print(output_checkboxes)
    #     assert input_checkboxes == output_checkboxes, 'Validating checked checkboxes in the hierarchy and output results'

    # def test_radio_button(self):
    #     radio_button = RadioButtonPage(self.driver)
    #     expected_output = radio_button.get_active_rbs_text()
    #     actual_output = radio_button.get_output_after_rb_click()
    #     assert expected_output == actual_output

    # def test_web_table(self):
    #     web_table = WebTablesPage(self.driver)
    #     submitted_person = web_table.submit_registration_form()
    #     # table_entries = web_table.get_table_entries()
    #     # print(submitted_person)
    #     # print(type(submitted_person))
    #     # print(table_entries)
    #     # print(type(table_entries))
    #     # print(type(submitted_person))
    #     # assert submitted_person in table_entries, 'Validating submitted form to display correct in table'

    # def test_web_table_search(self):
    #     web_table = WebTablesPage(self.driver)
    #     submitted_person = web_table.submit_registration_form()
    #     search_keyword = submitted_person[random.randint(0, 5)]
    #     web_table.fill_search_field(search_keyword)
    #     table_row = web_table.get_raw_text_by_delete_button()
    #     assert search_keyword in table_row, 'Validating that entering in search filed displays correct entry in the table'

    def test_rows_dropdown(self):
        web_table = WebTablesPage(self.driver)
        expected_rows_count = [5, 10, 20]
        rows_count = web_table.select_from_rows_dropdown()
        assert rows_count == expected_rows_count, 'Validating that slecting from rows dropdown changes the number of displayed rows in table'