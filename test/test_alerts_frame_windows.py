import random

import pytest

from pom.alerts_frame_windows_page import WindowsPage, AlertsPage
from pom.elements_page import *


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestBrowserWindowsPage:
    def test_new_tab(self):
        windows_page = WindowsPage(self.driver)
        windows_page.open_page()
        sample_page_header = "This is a sample page"
        new_tab_header_text = windows_page.get_new_window_text("tab")
        assert new_tab_header_text == sample_page_header, "Validating that text of newly opened tab is correct"

    def test_new_window(self):
        sample_page_header = "This is a sample page"
        windows_page = WindowsPage(self.driver)
        windows_page.open_page()
        new_tab_header_text = windows_page.get_new_window_text("window")
        assert new_tab_header_text == sample_page_header, "Validating that text of newly opened window is correct"


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestAlertsPage:
    def test_click_alert(self):
        alerts_page = AlertsPage(self.driver)
        alerts_page.open_page()
        expected_alert_text = "You clicked a button!"
        alert_text = alerts_page.check_click_alert()
        assert alert_text == expected_alert_text, "Validating that click alert text is correct"

    def test_timer_alert(self):
        alerts_page = AlertsPage(self.driver)
        alerts_page.open_page()
        is_alert_present = alerts_page.check_timer_alert(5.1)
        assert is_alert_present == True, "Validating that timer alert appears after 5 seconds"

    def test_confirm_alert(self):
        alerts_page = AlertsPage(self.driver)
        alerts_page.open_page()
        confirmation_options = ["Ok", "Cancel"]
        selected_option: str = confirmation_options[random.randint(0, 1)]
        confirmation_result_text = alerts_page.check_confirm_alert(selected_option)
        assert confirmation_result_text == f"You selected {selected_option}", "Validating the confirmation alert result is correct"

    def test_input_alert(self):
        alerts_page = AlertsPage(self.driver)
        alerts_page.open_page()
        input_name, prompt_result = alerts_page.check_prompt_alert()
        assert prompt_result == f"You entered {input_name}", "Validating prompt alert correct result"