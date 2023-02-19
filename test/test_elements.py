import pytest
from pom.elements_page import TextBoxPage, CheckBoxPage


@pytest.mark.usefixtures('setup')
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
