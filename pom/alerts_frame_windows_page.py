from base.base_page import BasePage
from locators.alerts_frame_windows_page_locators import *
from locators.demoqa_urls import AlertsFrameWindowsPageUrls


class AlertsFrameWindowsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AlertsFrameWindowsPageUrls.BROWSER_WINDOWS
        self.locators = BrowserWindowsPageLocators()

    def get_new_window_text(self, button_to_click: str):
        button_locators = {
            "tab": self.locators.NEW_TAB_BUTTON,
            "window": self.locators.NEW_WINDOW_BUTTON,
        }
        new_window_button = self.is_visible("css", button_locators[button_to_click], "Get new window button")
        new_window_button.click()
        self.switch_tab_by_handle(1)
        new_window_header_text = self.is_present("css", self.locators.NEW_WINDOW_HEADER,
                                              "Getting header text in the new window").text
        return new_window_header_text


