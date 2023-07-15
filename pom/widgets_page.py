import random
import time

from selenium.webdriver import Keys

from base.base_page import BasePage
from base.utils import Utils
from generator.generator import generate_date
from locators.demoqa_urls import WidgetsPageUrls
from locators.widgets_page_locators import *


class WidgetsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.ACCORDIAN
        self.locators = AccordianPageLocators()

    def check_accordian_section_content(self, section_num: str) -> list:
        accordian = {
            "first": [self.locators.FIRST_SECTION_TITLE, self.locators.FIRST_SECTION_BODY],
            "second": [self.locators.SECOND_SECTION_TITLE, self.locators.SECOND_SECTION_BODY],
            "third": [self.locators.THIRD_SECTION_TITLE, self.locators.THIRD_SECTION_BODY]
        }
        section_title = self.is_visible('css', accordian[section_num][0], "Get  section title")
        section_title.click()
        section_content = self.is_visible('css', accordian[section_num][1], "Get  section title").text
        return [section_title.text, section_content]


class AutoCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = WidgetsPageUrls.AUTO_COMPLETE
        self.locators = AutoCompletePageLocators()

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

    def fill_multiple_values_autocomplete(self, color_names: list) -> list:
        multiple_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_MULTIPLE,
                                                'Get multiple colors autocomplete field')
        for name in color_names:
            multiple_colors_field.send_keys(name)
            multiple_colors_field.send_keys(Keys.RETURN)
        name_inputs = self.are_present('css', self.locators.MULTIPLE_COLOR_NAMES_INPUTS,
                                       'Get multiple colors autocomplete field input values')
        return [input_name.text for input_name in name_inputs]

    def fill_single_values_autocomplete(self, color_names: list) -> str:
        single_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_SINGLE,
                                              'Get single color autocomplete field')
        for name in color_names:
            single_colors_field.send_keys(name)
            single_colors_field.send_keys(Keys.RETURN)
        name_input = self.is_present('css', self.locators.SINGLE_COLOR_NAME_INPUT,
                                     'Get single color autocomplete field input value')
        return name_input.text

    def get_autocomplete_values_number_after_delete(self):
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

    def select_date(self):
        date = next(generate_date())
        date_field = self.is_visible('css', self.locators.DATE_FIELD, 'Get date input')
        date_before = date_field.get_attribute('value')
        date_field.click()
        self.select_from_element_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.select_from_element_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.click_on_element_by_text(self.locators.DATE_SELECT_DAY_LIST, date.day)
        date_after = date_field.get_attribute('value')
        return date_before, date_after

    def select_date_time(self):
        date = next(generate_date())
        datetime_field = self.is_visible('css', self.locators.DATETIME_FIELD, 'Get date time input')
        datetime_before = datetime_field.get_attribute('value')
        datetime_field.click()
        self.is_visible('css', self.locators.DATETIME_SELECT_YEAR, 'Year dropdown').click()
        self.click_on_element_by_text(self.locators.DATETIME_SELECT_YEAR_LIST, str(random.randint(2018, 2028)))
        self.is_visible('css', self.locators.DATETIME_SELECT_MONTH, 'Month dropdown').click()
        self.click_on_element_by_text(self.locators.DATETIME_SELECT_MONTH_LIST, date.month)
        self.click_on_element_by_text(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.click_on_element_by_text(self.locators.DATETIME_SELECT_TIME_LIST, date.time)
        datetime_field = self.is_visible('css', self.locators.DATETIME_FIELD, 'Get date time input')
        datetime_after = datetime_field.get_attribute('value')
        return datetime_before, datetime_after
