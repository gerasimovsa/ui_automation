
import pytest
import allure
from pom.widgets_page import *


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Widgets Page")
class TestWidgetsPage:
    @allure.feature("Accordian")
    class TestAccordianPage:
        @allure.title("Accordian test")
        def test_accordian(self):
            widgets_page = WidgetsPage(self.driver)
            widgets_page.open_page()
            FIRST_SECTION_EXPECTED = ["What is Lorem Ipsum?", "Lorem Ipsum is simply dummy text"]
            SECOND_SECTION_EXPECTED = ["Where does it come from?",
                                       "It has roots in a piece of classical Latin literature from 45 BC"]
            THIRD_SECTION_EXPECTED = ["Why do we use it?",
                                      "It is a long established fact that a reader will be distracted"]
            second_section = widgets_page.check_accordian_section_content("second")
            third_section = widgets_page.check_accordian_section_content("third")
            first_section = widgets_page.check_accordian_section_content("first")
            assert first_section[0] == FIRST_SECTION_EXPECTED[0] and FIRST_SECTION_EXPECTED[1] in first_section[1]
            assert second_section[0] == SECOND_SECTION_EXPECTED[0] and SECOND_SECTION_EXPECTED[1] in second_section[1]
            assert third_section[0] == THIRD_SECTION_EXPECTED[0] and THIRD_SECTION_EXPECTED[1] in third_section[1]

    @allure.feature("Autocomplete")
    class TestAutocompletePage:
        @allure.title("Autocomplete test")
        def test_auto_complete_fields(self):
            auto_complete_page = AutoCompletePage(self.driver)
            auto_complete_page.open_page()
            color_names, trimmed_color_names = auto_complete_page.generate_trimmed_color_names()
            multiple_input_names = auto_complete_page.fill_multiple_values_autocomplete(trimmed_color_names)
            single_input_name = auto_complete_page.fill_single_values_autocomplete(trimmed_color_names)
            assert multiple_input_names == color_names, "Validating that multi-value auto complete field works"
            assert multiple_input_names[-1] == single_input_name, "Validating that single-value auto complete field works"
            values_number_before_delete, values_number_after_delete = auto_complete_page.get_autocomplete_values_after_delete()
            assert values_number_before_delete > values_number_after_delete, "Validating that value can be removed"

    @allure.feature("Date Picker")
    class TestDatePickerPage:
        @allure.title("Date Picker test")
        def test_date_picker(self):  # rework later to check exact date
            date_picker_page = DataPickerPage(self.driver)
            date_picker_page.open_page()
            date_value, updated_date = date_picker_page.select_date()
            assert date_value != updated_date, "Validating that date field value changes after input"

        @allure.title("New tab test")
        def test_date_time_picker(self):  # rework later to check exact date
            date_picker_page = DataPickerPage(self.driver)
            date_picker_page.open_page()
            datetime_value, updated_datetime = date_picker_page.select_date_time()
            assert datetime_value != updated_datetime, "Validating that datetime field value changes after input"

    @allure.feature("Slider")
    class TestSliderPage:
        @allure.title("Slider test")
        def test_slider(self):
            slider_page = SliderPage(self.driver)
            slider_page.open_page()
            value_to_add = random.randint(1, 75)
            slider_value, slider_field_value = slider_page.increase_slider_value(value_to_add)
            expected_slider_value = int(slider_value) + value_to_add
            assert int(slider_field_value) == expected_slider_value, "Validating that slider value can be increased"

    @allure.feature("Progress Bar")
    class TestProgressBarPage:
        @allure.title("Progress Bar test")
        def test_progress_bar_start_reset(self):
            progress_bar_page = ProgressBarPage(self.driver)
            progress_bar_page.open_page()
            progress_bar_after_complete, progress_bar_after_reset = progress_bar_page.reset_progress_bar()
            assert int(progress_bar_after_complete) == 100, "Validating that progress bar values completes"
            assert int(progress_bar_after_reset) == 0, "Validating that progress bar values resets"

    @allure.feature("Tabs")
    class TestTabsPage:
        @allure.title("Tabs test")
        def test_tabs(self):
            tabs_page = TabsPage(self.driver)
            tabs_page.open_page()
            EXPECTED_TABS_TEXT = [
                ("What", "Lorem Ipsum is simply dummy text"),
                ("Origin", "It has roots in a piece of classical Latin literature from 45 BC"),
                ("Use",
                 "Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text")
            ]
            tabs_title_body_text = tabs_page.check_tabs()
            assert EXPECTED_TABS_TEXT[2][0] == tabs_title_body_text[0][0] and EXPECTED_TABS_TEXT[2][1] in \
                   tabs_title_body_text[0][1] \
                , "Validating third tab title and content"
            assert EXPECTED_TABS_TEXT[1][0] == tabs_title_body_text[1][0] and EXPECTED_TABS_TEXT[1][1] in \
                   tabs_title_body_text[1][1], \
                "Validating second tab title and content"
            assert EXPECTED_TABS_TEXT[0][0] == tabs_title_body_text[2][0] and EXPECTED_TABS_TEXT[0][1] in \
                   tabs_title_body_text[2][1], \
                "Validating first tab title and content"

    @allure.feature("Tooltips")
    class TestTooltipsPage:
        @allure.title("Tooltips test")
        def test_tooltips(self):
            tooltips_page = TooltipsPage(self.driver)
            tooltips_page.open_page()
            EXPECTED_TOOLTIPS_TEXT = [
                'You hovered over the Button',
                'You hovered over the text field',
                'You hovered over the Contrary',
                'You hovered over the 1.10.32']
            tooltips_text = tooltips_page.check_tooltips()
            assert tooltips_text == EXPECTED_TOOLTIPS_TEXT, "Validating that tooltips are correct"

    @allure.feature("Menu")
    class TestMenuPage:
        @allure.title("Menu test")
        def test_menu(self):
            menu_page = MenuPage(self.driver)
            menu_page.open_page()
            EXPECTED_ITEMS_TEXT = ['Main Item 1',
                                   'Main Item 2',
                                   'Sub Item',
                                   'Sub Item',
                                   'SUB SUB LIST »',
                                   'Sub Sub Item 1',
                                   'Sub Sub Item 2',
                                   'Main Item 3']
            items_text = menu_page.check_menu_items()
            assert items_text == EXPECTED_ITEMS_TEXT, "Validating that items of menu have a correct text"

    @allure.feature("Select Menu")
    class TestSelectMenuPage:
        @allure.title("Select Menu test")
        def test_select_menu(self):
            select_menu_page = SelectMenuPage(self.driver)
            select_menu_page.open_page()

            select_input_value, select_current_value = select_menu_page.check_select_value()
            assert select_input_value in select_current_value, "Validating select value field"

            select_one_input_value, select_one_current_value = select_menu_page.check_one_value()
            assert select_one_input_value in select_one_current_value, "Validating select one value field"

            expected_color, selected_color = select_menu_page.check_old_style_select()
            assert selected_color == expected_color, "Validating old style select list"

            colors_list, selected_colors_list = select_menu_page.check_multiselect_dropdown()
            assert selected_colors_list == colors_list, "Validating multiselect dropdown values field"

            items_removed_status = select_menu_page.are_multiselected_items_removed()
            assert items_removed_status is True, "Validating that items from multiselect dropdown are removed"

            expected_options, selected_options = select_menu_page.check_standart_multiselect()
            assert selected_options == expected_options, "Validating standard multiselect list"
