import allure
import pytest

from pom.alerts_frame_windows_page import *
from pom.elements_page import *


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Alerts, Frame & Windows Page")
class AlertsFrameWindowsPage:
    @allure.feature("Browser Windows")
    class TestBrowserWindowsPage:
        @allure.title("New tab test")
        def test_new_tab(self):
            windows_page = WindowsPage(self.driver)
            windows_page.open_page()
            sample_page_header = "This is a sample page"
            new_tab_header_text = windows_page.get_new_window_text("tab")
            assert new_tab_header_text == sample_page_header, "Validating that text of newly opened tab is correct"

        @allure.title("New window test")
        def test_new_window(self):
            sample_page_header = "This is a sample page"
            windows_page = WindowsPage(self.driver)
            windows_page.open_page()
            new_tab_header_text = windows_page.get_new_window_text("window")
            assert new_tab_header_text == sample_page_header, "Validating that text of newly opened window is correct"

    @allure.feature("Alerts")
    class TestAlertsPage:
        @allure.title("Click alert test")
        def test_click_alert(self):
            alerts_page = AlertsPage(self.driver)
            alerts_page.open_page()
            EXPECTED_ALERT_TEXT = "You clicked a button!"
            alert_text = alerts_page.check_click_alert()
            assert alert_text == EXPECTED_ALERT_TEXT, "Validating that click alert text is correct"

        @allure.title("Timer alert test")
        def test_timer_alert(self):
            alerts_page = AlertsPage(self.driver)
            alerts_page.open_page()
            is_alert_present = alerts_page.check_timer_alert(5.1)
            assert is_alert_present is True, "Validating that timer alert appears after 5 seconds"

        @allure.title("Confirm alert test")
        def test_confirm_alert(self):
            alerts_page = AlertsPage(self.driver)
            alerts_page.open_page()
            confirmation_options = ["Ok", "Cancel"]
            selected_option: str = confirmation_options[random.randint(0, 1)]
            confirmation_result_text = alerts_page.check_confirm_alert(selected_option)
            assert selected_option in confirmation_result_text, "Validating the confirmation alert result is correct"

        @allure.title("Input alert test")
        def test_input_alert(self):
            alerts_page = AlertsPage(self.driver)
            alerts_page.open_page()
            input_name, prompt_result = alerts_page.check_prompt_alert()
            assert input_name in prompt_result, "Validating prompt alert correct result"

    @allure.feature("Frames")
    class TestFramesPage:
        @allure.title("Frames test")
        def test_frames(self):
            frames_page = FramesPage(self.driver)
            frames_page.open_page()
            EXPECTED_FRAME_1 = ['This is a sample page', '500px', '350px']
            EXPECTED_FRAME_2 = ['This is a sample page', '100px', '100px']
            frame1 = frames_page.check_frame(1)
            frame2 = frames_page.check_frame(2)
            assert frame1 == EXPECTED_FRAME_1, "Validating that frame 1 size and text are correct"
            assert frame2 == EXPECTED_FRAME_2, "Validating that frame 2 size and text are correct"

    @allure.feature("Nested Frames")
    class TestNestedFramesPage:
        @allure.title("Nested frames test")
        def test_nested_frames(self):
            nested_frames_page = NestedFramesPage(self.driver)
            nested_frames_page.open_page()
            EXPECTED_PARENT_FRAME_TEXT = "Parent frame"
            EXPECTED_CHILD_FRAME_TEXT = "Child Iframe"
            parent_text, child_text = nested_frames_page.check_nested_frame()
            assert parent_text == EXPECTED_PARENT_FRAME_TEXT, "Validating parent frame text"
            assert child_text == EXPECTED_CHILD_FRAME_TEXT, "Validating nested child frame text"

    @allure.feature("Modal Dialogs")
    class TestModalDialogsPage:
        @allure.title("Modal dialogs test")
        def test_modal_dialogs(self):
            modal_dialogs_page = ModalDialogsPage(self.driver)
            EXPECTED_SMALL_MODAL = ('Small Modal', 47)
            EXPECTED_LARGE_MODAL = ('Large Modal', 574)
            modal_dialogs_page.open_page()
            modal_dialogs = modal_dialogs_page.check_modal_windows()
            assert modal_dialogs == [EXPECTED_SMALL_MODAL, EXPECTED_LARGE_MODAL], "Validating small and large modals"
