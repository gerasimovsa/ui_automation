import pytest

from pom.alerts_frame_windows_page import AlertsFrameWindowsPage
from pom.elements_page import *


@pytest.mark.usefixtures('setup')  # split up in classes later
class TestBrowserWindowsPage:
    def test_new_tab(self):
        windows_page = AlertsFrameWindowsPage(self.driver)
        windows_page.open_page()
        sample_page_header = "This is a sample page"
        new_tab_header_text = windows_page.get_new_window_text("tab")
        assert new_tab_header_text == sample_page_header, "Validating that text of newly opened tab is correct"

    def test_new_window(self):
        sample_page_header = "This is a sample page"
        windows_page = AlertsFrameWindowsPage(self.driver)
        windows_page.open_page()
        new_tab_header_text = windows_page.get_new_window_text("window")
        assert new_tab_header_text == sample_page_header, "Validating that text of newly opened window is correct"

@pytest.mark.usefixtures('setup')  # split up in classes later
class TestAlertsPage:
    def test_new_tab(self):
        windows_page = AlertsFrameWindowsPage(self.driver)
        windows_page.open_page()