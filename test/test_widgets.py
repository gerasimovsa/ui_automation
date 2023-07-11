import time

import pytest
from pom.widgets_page import *


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestWidgetsPage:
    def test_accordian_page(self):
        widgets_page = WidgetsPage(self.driver)
        widgets_page.open_page()
        FIRST_SECTION_EXPECTED = ["What is Lorem Ipsum?", "Lorem Ipsum is simply dummy text"]
        SECOND_SECTION_EXPECTED = ["Where does it come from?", "It has roots in a piece of classical Latin literature from 45 BC"]
        THIRD_SECTION_EXPECTED = ["Why do we use it?", "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text"]
        first_section = widgets_page.check_accordian_section_content("first")
        second_section = widgets_page.check_accordian_section_content("second")
        third_section = widgets_page.check_accordian_section_content("third")
        assert first_section[0] == FIRST_SECTION_EXPECTED[0] and FIRST_SECTION_EXPECTED[1] in first_section[1]
        assert second_section[0] == SECOND_SECTION_EXPECTED[0] and SECOND_SECTION_EXPECTED[1] in second_section[1]
        assert third_section[0] == THIRD_SECTION_EXPECTED[0] and THIRD_SECTION_EXPECTED[1] in third_section[1]

    def test_auto_complete_page(self):
        auto_complete_page = AutoCompletePage(self.driver)
        auto_complete_page.open_page()
        color_names, trimmed_color_names = auto_complete_page.generate_trimmed_color_names()
        multiple_input_names = auto_complete_page.fill_multiple_values_autocomplete(trimmed_color_names)
        single_input_name = auto_complete_page.fill_single_values_autocomplete(trimmed_color_names)
        assert multiple_input_names == color_names, "Validating that multi-value auto complete field works"
        assert multiple_input_names[-1] == single_input_name, "Validating that single-value auto complete field works"
