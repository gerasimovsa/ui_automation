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
        return self.check_alert_is_present(time_to_wait)

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





