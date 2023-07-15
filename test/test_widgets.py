
import pytest
from pom.widgets_page import *


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestWidgetsPage:
    def test_accordian(self):
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

    def test_auto_complete_fields(self):
        auto_complete_page = AutoCompletePage(self.driver)
        auto_complete_page.open_page()
        color_names, trimmed_color_names = auto_complete_page.generate_trimmed_color_names()
        multiple_input_names = auto_complete_page.fill_multiple_values_autocomplete(trimmed_color_names)
        single_input_name = auto_complete_page.fill_single_values_autocomplete(trimmed_color_names)
        assert multiple_input_names == color_names, "Validating that multi-value auto complete field works"
        assert multiple_input_names[-1] == single_input_name, "Validating that single-value auto complete field works"
        values_number_before_delete, values_number_after_delete = auto_complete_page.get_autocomplete_values_number_after_delete()
        assert values_number_before_delete > values_number_after_delete, "Validating that value can be removed"

    def test_date_picker(self):                                                                                         #rework later to check exact date
        date_picker_page = DataPickerPage(self.driver)
        date_picker_page.open_page()
        date_value, updated_date = date_picker_page.select_date()
        assert date_value != updated_date, "Validating that date field value changes after input"

    def test_date_time_picker(self):                                                                                    #rework later to check exact date
        date_picker_page = DataPickerPage(self.driver)
        date_picker_page.open_page()
        datetime_value, updated_datetime = date_picker_page.select_date_time()
        assert datetime_value != updated_datetime, "Validating that datetime field value changes after input"
