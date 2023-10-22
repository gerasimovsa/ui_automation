import pytest
import allure
from pom.elements_page import *


@pytest.mark.usefixtures('setup')
@allure.suite("Elements Page")
class TestElementsPage:
    @allure.feature("Text Box")
    class TestTextBox:
        @allure.title("Text Box test")
        def test_text_box(self):
            text_box_page = TextBoxPage(self.driver)
            text_box_page.open_page()
            expected_output_forms_text = text_box_page.fill_all_fields()
            output_forms_text = text_box_page.get_output_forms_text()
            assert expected_output_forms_text == output_forms_text, 'Validating Elements page forms output text'

    @allure.feature("Check Box")
    class TestCheckBox:
        @allure.title("Text Box test")
        def test_checkbox(self):
            checkbox = CheckBoxPage(self.driver)
            checkbox.open_page()
            checkbox.expand_checkbox_list()
            checkbox.click_random_checkboxes()
            input_checkboxes = checkbox.get_checked_checkboxes_text()
            output_checkboxes = checkbox.get_output_results_text()
            print(input_checkboxes)
            print(output_checkboxes)
            assert input_checkboxes == output_checkboxes, 'Validating checked checkboxes in the hierarchy and output results'

    @allure.feature("Radio Button")
    class TestRadioButton:
        @allure.title("Radio Button test")
        def test_radio_button(self):
            radio_button = RadioButtonPage(self.driver)
            radio_button.open_page()
            expected_output = radio_button.get_active_rbs_text()
            actual_output = radio_button.get_output_after_rb_click()
            assert expected_output == actual_output

    @allure.feature("Web Table")
    class TestWebTable:
        @allure.title("Web Table test")
        def test_web_table(self):
            web_table = WebTablesPage(self.driver)
            web_table.open_page()
            submitted_person = web_table.submit_registration_form()
            table_entries = web_table.get_table_entries()
            assert submitted_person in table_entries, 'Validating submitted form to display correct in table'

        @allure.title("Table search test")
        def test_web_table_search(self):
            web_table = WebTablesPage(self.driver)
            web_table.open_page()
            submitted_person = web_table.submit_registration_form()
            search_keyword = submitted_person[random.randint(0, 5)]
            web_table.fill_search_field(search_keyword)
            table_row = web_table.get_raw_text_by_delete_button()
            assert search_keyword in table_row, 'Validating that entering in search filed displays correct entry in the table'

        @allure.title("Rows dropdown test")
        def test_rows_dropdown(self):
            web_table = WebTablesPage(self.driver)
            web_table.open_page()
            expected_rows_count = [5, 10, 20]
            rows_count = web_table.select_from_rows_dropdown()
            assert rows_count == expected_rows_count, 'Validating that selecting from rows dropdown changes the number of displayed rows in table'

    @allure.feature("Buttons Page")
    class TestButtonsPage:
        @allure.title("Button test")
        def test_click_buttons(self):
            buttons_page = ButtonsPage(self.driver)
            buttons_page.open_page()
            buttons = buttons_page.BUTTONS
            success_click_text = buttons_page.SUCCESS_CLICK_TEXT
            for button in buttons:
                success = buttons_page.click_on_each_button(button)
                assert success in success_click_text, 'Validating if success text is present in expected success text list'

    @allure.feature("Links Page")
    class TestLinksPage:
        @allure.title("Home link test")
        def test_home_link(self):
            links_page = LinksPage(self.driver)
            links_page.open_page()
            home_link_href, current_url = links_page.check_home_link()
            assert current_url == home_link_href, 'Validating that url of new tab matches href url'

        @allure.title("API calls test")
        def test_api_calls(self):
            links_page = LinksPage(self.driver)
            links_page.open_page()
            expected_status_message = links_page.get_api_call_links_text()
            response_code, response_message = links_page.check_api_call_links()
            expected_status_code = links_page.send_calls_get_status_code()
            for k, v in zip(expected_status_message, response_message):
                assert k in v, 'Validating that response message corresponds to link text '
            assert response_code == expected_status_code, 'Validating that status code corresponds to URL status code'

    @allure.feature("Upload Download Page")
    class TestUploadDownloadPage:
        @allure.title("Upload and download test")
        def test_upload_download_page(self):
            upload_download_page = UploadDownloadPage(self.driver)
            upload_download_page.open_page()
            file_name, uploaded_file_name = upload_download_page.upload_file()
            assert file_name == uploaded_file_name, 'Validating that uploaded filename matches result'
            check = upload_download_page.download_file()
            assert check is True, "Validating image download link"

    @allure.feature("Dynamic Properties Page")
    class DynamicPropertiesPage:
        @allure.title("Change color of the button test")
        def test_button_color_change(self):
            dynamic_props_page = DynamicPropsPage(self.driver)
            dynamic_props_page.open_page()
            expected_color = dynamic_props_page.RED_COLOR
            dynamic_props_page.open_page()
            start_time = time.time()
            button_color = dynamic_props_page.check_color_change_after()
            delta = time.time() - start_time
            print(f'Approximate elapsed time until color changed: {delta}')
            assert delta <= 5, f'Approximate elapsed time until color changed is greater then 5 seconds. Actual: {delta}'
            assert button_color == expected_color, 'Validating that color of button changed'

        @allure.title("Dynamic states test")
        def test_dynamic_states(self):
            dynamic_props_page = DynamicPropsPage(self.driver)
            timeout = 5.1
            dynamic_props_page.open_page()
            is_visible = dynamic_props_page.check_button_is_visible_after(timeout)
            assert is_visible is True
            is_clickable = dynamic_props_page.check_button_is_clickable_after(timeout)
            assert is_clickable is True
