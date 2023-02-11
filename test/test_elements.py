import time
import pytest
from pom.elements_page import TextBoxPage


@pytest.mark.usefixtures('setup')
class TestElementsPage:

    def test_elements_page_field(self):
        text_box_page = TextBoxPage(self.driver)
        expected_output_forms_text = text_box_page.fill_all_fields()
        time.sleep(2)
        output_forms_text = text_box_page.get_output_forms_text()
        assert expected_output_forms_text == output_forms_text, 'Validating Elements page forms output text'
