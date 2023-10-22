import random

import allure
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from base.base_page import BasePage
from base.utils import Utils
from generator.generator import generate_date
from locators.demoqa_urls import WidgetsPageUrls
from locators.widgets_page_locators import *
from selenium.webdriver.support.select import Select


class WidgetsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.ACCORDIAN
        self.locators = AccordianPageLocators()

    @allure.step("Getting title and content of accordian tabs")
    def check_accordian_section_content(self, section_num: str) -> list:
        accordian = {
            "first": [self.locators.FIRST_SECTION_TITLE, self.locators.FIRST_SECTION_BODY],
            "second": [self.locators.SECOND_SECTION_TITLE, self.locators.SECOND_SECTION_BODY],
            "third": [self.locators.THIRD_SECTION_TITLE, self.locators.THIRD_SECTION_BODY]
        }
        section_title = self.is_visible('css', accordian[section_num][0], "Get  section title")
        section_title.click()
        section_content = self.is_visible('css', accordian[section_num][1], "Get  section body").text
        return [section_title.text, section_content]


class AutoCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.AUTO_COMPLETE
        self.locators = AutoCompletePageLocators()

    @allure.step("Trim color name")
    def generate_trimmed_color_names(self) -> list:
        color_names = ["Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta",
                       "Aqua"]  # try to implement via the dataclass
        count = random.randint(1, 11)
        multiple_color_names = []
        while count > 0:
            random_name_index = random.randint(0, len(color_names) - 1)
            color_name = color_names.pop(random_name_index)
            multiple_color_names.append(color_name)
            count -= 1
        return multiple_color_names, [Utils.trim_string_end(name) for name in multiple_color_names]

    @allure.step("Fill multiple value autocomplete with color names")
    def fill_multiple_values_autocomplete(self, color_names: list) -> list:
        multiple_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_MULTIPLE,
                                                'Get multiple colors autocomplete field')
        for name in color_names:
            multiple_colors_field.send_keys(name)
            multiple_colors_field.send_keys(Keys.RETURN)
        name_inputs = self.are_present('css', self.locators.MULTIPLE_COLOR_NAMES_INPUTS,
                                       'Get multiple colors autocomplete field input values')
        return [input_name.text for input_name in name_inputs]

    @allure.step("Fill single value autocomplete with color name")
    def fill_single_values_autocomplete(self, color_names: list) -> str:
        single_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_SINGLE,
                                              'Get single color autocomplete field')
        for name in color_names:
            single_colors_field.send_keys(name)
            single_colors_field.send_keys(Keys.RETURN)
        name_input = self.is_present('css', self.locators.SINGLE_COLOR_NAME_INPUT,
                                     'Get single color autocomplete field input value')
        return name_input.text

    @allure.step("Get field values after deleting one")
    def get_autocomplete_values_after_delete(self):
        name_inputs = self.are_present('css', self.locators.MULTIPLE_COLOR_NAMES_INPUTS,
                                       'Get multiple colors autocomplete field input values')
        number_before_delete = len(name_inputs)
        remove_buttons = self.are_present('css', self.locators.REMOVE_COLOR_NAME,
                                          'Get remove buttons of autocomplete values')
        remove_buttons[random.randint(0, number_before_delete - 1)].click()
        name_inputs = self.are_present('css', self.locators.MULTIPLE_COLOR_NAMES_INPUTS,
                                       'Get multiple colors autocomplete field input values')
        number_after_delete = len(name_inputs)
        return number_before_delete, number_after_delete


class DataPickerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.DATE_PICKER
        self.locators = DatePickerLocators()

    @allure.step("Selecting date")
    def select_date(self):
        date = next(generate_date())
        date_field = self.is_visible('css', self.locators.DATE_FIELD, 'Get date input')
        date_before = date_field.get_attribute('value')
        date_field.click()
        self.select_from_element_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_from_element_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.click_on_element_with_text(self.locators.DATE_SELECT_DAY_LIST, date.day)
        date_after = date_field.get_attribute('value')
        return date_before, date_after

    @allure.step("Selecting date and time")
    def select_date_time(self):
        date = next(generate_date())
        datetime_field = self.is_visible('css', self.locators.DATETIME_FIELD, 'Get date time input')
        datetime_before = datetime_field.get_attribute('value')
        datetime_field.click()
        self.is_visible('css', self.locators.DATETIME_SELECT_YEAR, 'Year dropdown').click()
        self.click_on_element_with_text(self.locators.DATETIME_SELECT_YEAR_LIST, str(random.randint(2018, 2028)))
        self.is_visible('css', self.locators.DATETIME_SELECT_MONTH, 'Month dropdown').click()
        self.click_on_element_with_text(self.locators.DATETIME_SELECT_MONTH_LIST, date.month)
        self.click_on_element_with_text(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.click_on_element_with_text(self.locators.DATETIME_SELECT_TIME_LIST, date.time)
        datetime_field = self.is_visible('css', self.locators.DATETIME_FIELD, 'Get date time input')
        datetime_after = datetime_field.get_attribute('value')
        return datetime_before, datetime_after


class SliderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.SLIDER
        self.locators = SliderLocators()

    @allure.step("Sending right key to increase slider value")
    def increase_slider_value(self, count: int):
        slider = self.is_visible('css', self.locators.SLIDER, "Getting slider")
        slider_value = slider.get_attribute('value')
        while count > 0:
            slider.send_keys(Keys.RIGHT)
            count -= 1
        slider_field = self.is_visible('css', self.locators.SLIDER, "Getting slider form field")
        slider_field_value = slider_field.get_attribute('value')
        return slider_value, slider_field_value


class ProgressBarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.PROGRESS_BAR
        self.locators = ProgressBarLocators()

    @allure.step("Reset progress bar after starting the progress")
    def reset_progress_bar(self):
        progress_bar = self.is_present('css', self.locators.PROGRESS_BAR, "Getting progress bar")
        start_button = self.is_visible('css', self.locators.START_STOP_BUTTON, "Getting start button")
        start_button.click()
        reset_button_is_present = self.check_element_state_after_time('css', self.locators.RESET_BUTTON, 'present', 12)
        if reset_button_is_present:
            progress_bar_value = progress_bar.get_attribute('aria-valuenow')
            self.is_visible('css', self.locators.RESET_BUTTON, "Clicking on reset button").click()
        else:
            pass
        reset_progress_bar_value = progress_bar.get_attribute('aria-valuenow')
        return progress_bar_value, reset_progress_bar_value


class TabsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.TABS
        self.locators = TabsLocators()

    @allure.step("Getting text of the tabs")
    def check_tabs(self) -> list:
        tabs_text = []
        tabs = {
            "third": [self.locators.THIRD_TAB_TITLE, self.locators.THIRD_TAB_BODY],
            "second": [self.locators.SECOND_TAB_TITLE, self.locators.SECOND_TAB_BODY],
            "first": [self.locators.FIRST_TAB_TITLE, self.locators.FIRST_TAB_BODY]
        }
        for k, v in tabs.items():
            title = self.is_visible('css', v[0], "Get tab title")
            title.click()
            body = self.is_visible('css', v[1], "Get tab body")
            tabs_text.append((title.text, body.text))
        return tabs_text


class TooltipsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.TOOLTIPS
        self.locators = TooltipsLocators()

    @allure.step("Getting tooltip text")
    def check_tooltips(self) -> list:
        tooltips_text = []
        tooltip_element_locators = [
            (self.locators.HOVER_BUTTON, self.locators.TOOLTIP_BUTTON),
            (self.locators.HOVER_FIELD, self.locators.TOOLTIP_FIELD),
            (self.locators.HOVER_LINK_TEXT, self.locators.TOOLTIP_LINK_TEXT),
            (self.locators.HOVER_LINK_NUMBERS, self.locators.TOOLTIP_LINK_NUMBERS)
        ]
        for item in tooltip_element_locators:
            element = self.is_visible('xpath', item[0], "Get tooltip of element")
            self.move_to_element(element)
            self.is_present('css', item[1], "State of hovered element is changed to 'Showing tooltip'")
            tooltip_text = self.is_visible('css', self.locators.ACTIVE_TOOLTIP, "Get tooltip text").text
            tooltips_text.append(tooltip_text)
        return tooltips_text


class MenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.MENU
        self.locators = MenuLocators()

    @allure.step("Getting text of menu items")
    def check_menu_items(self) -> list:
        items_text = []
        menu_items_list = self.are_present('css', self.locators.MENU_ITEMS, "Getting all the menu items")
        for item in menu_items_list:
            self.move_to_element(item)
            items_text.append(item.text)
        return items_text


class SelectMenuPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.SELECT_MENU
        self.locators = SelectMenuLocators()

    @allure.step("Selecting random options in select menu")
    def check_select_value(self) -> str:
        single_select_values = [
            "Group 1, option 1",
            "Group 1, option 2",
            "Group 2, option 1",
            "Group 2, option 2",
            "A root option",
            "Another root option"
        ]
        random_value = single_select_values[random.randint(0, 5)]
        single_select = self.is_visible('css', self.locators.SELECT_VALUE_DROPDOWN, "Select value input")
        single_select.send_keys(random_value)
        single_select.send_keys(Keys.RETURN)
        current_value = self.is_present('xpath', self.locators.SELECT_VALUE_DROPDOWN_RESULT, "Select value result").text
        return random_value, current_value

    @allure.step("Selecting one option in select menu")
    def check_one_value(self) -> str:
        select_one_values = ["Dr.", "Mr.", "Mrs.", "Ms.", "Prof.", "Other"]
        random_select_one_value = select_one_values[random.randint(0, 5)]
        select_one = self.is_visible('css', self.locators.SELECT_ONE_DROPDOWN, "Select one input")
        select_one.send_keys(random_select_one_value)
        select_one.send_keys(Keys.RETURN)
        current_select_one_value = self.is_present('xpath', self.locators.SELECT_ONE_DROPDOWN_RESULT,
                                                   "Select one result").text
        return random_select_one_value, current_select_one_value

    @allure.step("Selecting in old style select")
    def check_old_style_select(self) -> str:
        color_names = {
            "1": "Blue", "2": "Green", "3": "Yellow", "4": "Purple", "5": "Black", "6": "White", "7": "Voilet",
            "8": "Indigo", "9": "Magenta",
            "10": "Aqua"
        }
        random_value = str(random.randint(1, 10))
        old_select = self.is_visible('css', self.locators.OLD_SELECT, "Getting old style select")
        Select(old_select).select_by_value(random_value)
        selected_colors_list = Select(old_select).all_selected_options
        selected_colors = self.get_text_from_webelements(selected_colors_list)
        return color_names[random_value].lower(), selected_colors[0]

    @allure.step("Selecting in multiselect dropdown")
    def check_multiselect_dropdown(self) -> list:
        color_names = ["Red", "Blue", "Green", "Black"]
        multiselect_dropdown = self.is_visible('css', self.locators.MULTISELECT_DROPDOWN,
                                               "Getting multiselect dropdown")
        for color in color_names:
            multiselect_dropdown.send_keys(color)
            multiselect_dropdown.send_keys(Keys.RETURN)
        selected_colors = self.are_present('css', self.locators.MULTISELECT_DROPDOWN_RESULTS, "Multiselect results")
        return color_names, [color.text for color in selected_colors]

    @allure.step("Are items removed from selection")
    def are_multiselected_items_removed(self) -> bool:
        remove_buttons = self.are_present('css', self.locators.REMOVE_ELEMENT_FROM_MULTISELECT, "Getting remove buttons")
        for button in remove_buttons:
            button.click()
        try:
            self.are_visible('css', self.locators.MULTISELECT_DROPDOWN_RESULTS, "Multiselect results")
            return False
        except TimeoutException as error:
            print(f'{error}\n Items of multiselect dropdown are removed')
            return True

    @allure.step("Selecting in standard multiselect")
    def check_standart_multiselect(self) -> list:
        option_values = ["volvo", "saab", "opel", "audi"]
        standard_select = self.is_visible('css', self.locators.STANDART_SELECT, "Getting standart select")
        for option in option_values:
            Select(standard_select).select_by_value(option)
        selected_options_list = Select(standard_select).all_selected_options
        selected_options = self.get_text_from_webelements(selected_options_list)
        return option_values, selected_options


