from base.base_page import BasePage
from generator.generator import *
from locators.alerts_frame_windows_page_locators import *
from locators.demoqa_urls import AlertsFrameWindowsPageUrls


class WindowsPage(BasePage):
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


class AlertsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AlertsFrameWindowsPageUrls.ALERTS
        self.locators = AlertsPageLocators()

    def check_click_alert(self) -> str:
        alert_click_button = self.is_visible("css", self.locators.ALERT_BUTTON, "Get click alert button")
        alert_click_button.click()
        alert_text = self.get_alert_text()
        return alert_text

    def check_timer_alert(self, time_to_wait: float) -> bool:
        alert_timer_button = self.is_visible("css", self.locators.TIMER_ALERT_BUTTON, "Get timer alert button")
        alert_timer_button.click()
        return self.check_alert_is_present_after_time(time_to_wait)

    def check_confirm_alert(self, option: str) -> str:
        alert_confirmation_button = self.is_visible("css", self.locators.CONFIRM_BUTTON, "Get confirm alert button")
        alert_confirmation_button.click()
        confirmation_alert = self.driver.switch_to.alert
        if option == "Ok":
            confirmation_alert.accept()
        elif option == "Cancel":
            confirmation_alert.dismiss()
        else:
            return "No option for confirmation alert is selected!"
        confirmation_result = self.is_visible("css", self.locators.CONFIRM_RESULT,
                                              "Get confirm result field text").text
        return confirmation_result

    def check_prompt_alert(self) -> str:
        prompt_alert_button = self.is_visible("css", self.locators.PROMPT_BUTTON, "Get prompt alert button")
        prompt_alert_button.click()
        person_info = next(generated_person())
        full_name = person_info.last_name + " " + person_info.last_name
        prompt_alert = self.driver.switch_to.alert
        prompt_alert.send_keys(full_name)
        prompt_alert.accept()
        prompt_result_text = self.is_visible("css", self.locators.PROMPT_RESULT, "Get prompt result field text").text
        return full_name, prompt_result_text


class FramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AlertsFrameWindowsPageUrls.FRAMES
        self.locators = FramesPageLocators()

    def check_frame(self, frame_num: int) -> list:
        if frame_num == 1:
            frame = self.is_present("css", self.locators.FRAME_1, "Get the first frame")
        elif frame_num == 2:
            frame = self.is_present("css", self.locators.FRAME_2, "Get the second frame")
        width = frame.get_attribute("width")
        height = frame.get_attribute("height")
        self.driver.switch_to.frame(frame)
        text = self.is_present("css", self.locators.TITLE_FRAME, "Get the frame text").text
        self.driver.switch_to.default_content()
        return [text, width, height]


class NestedFramesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AlertsFrameWindowsPageUrls.NESTED_FRAMES
        self.locators = NestedFramesPageLocators()

    def check_nested_frame(self) -> str:
        parent_frame = self.is_present("css", self.locators.PARENT_FRAME, "Get the parent frame")
        self.driver.switch_to.frame(parent_frame)
        parent_text = self.is_present("css", self.locators.PARENT_FRAME_TEXT, "Get the parent frame text").text
        child_frame = self.is_present("css", self.locators.CHILD_FRAME, "Get the child frame")
        self.driver.switch_to.frame(child_frame)
        child_text = self.is_present("css", self.locators.CHILD_FRAME_TEXT, "Get the child frame text").text
        return parent_text, child_text


class ModalDialogsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = AlertsFrameWindowsPageUrls.MODAL_DIALOGS
        self.locators = ModalDialogsPageLocators()

    def check_modal_windows(self) -> list:
        small_modal_button = self.is_present("css", self.locators.SMALL_MODAL_BUTTON, "Get the small modal button")
        small_modal_button.click()
        small_modal_title = self.is_present("css", self.locators.TITLE_SMALL_MODAL, "Get the small modal window title").text
        small_modal_text = self.is_visible("css", self.locators.BODY_SMALL_MODAL, "Get the small modal window text").text
        close_small_modal_button = self.is_present("css", self.locators.SMALL_MODAL_CLOSE_BUTTON, "Get the small modal close button")
        close_small_modal_button.click()
        large_modal_button = self.is_present("css", self.locators.LARGE_MODAL_BUTTON, "Get the large modal button")
        large_modal_button.click()
        large_modal_title = self.is_visible("css", self.locators.TITLE_LARGE_MODAL, "Get the large modal window title").text
        large_modal_text = self.is_present("css", self.locators.BODY_LARGE_MODAL, "Get the large modal window text").text
        close_large_modal_button = self.is_present("css", self.locators.LARGE_MODAL_CLOSE_BUTTON, "Get the large modal close button")
        close_large_modal_button.click()
        return [(small_modal_title, len(small_modal_text)), (large_modal_title, len(large_modal_text))]




