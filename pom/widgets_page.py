import random
import time

from selenium.webdriver import Keys

from base.base_page import BasePage
from base.utils import Utils
from locators.widgets_page_locators import AccordianPageLocators, AutoCompletePageLocators
from locators.demoqa_urls import WidgetsPageUrls


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
                       "Aqua"]
        count = random.randint(1, 11)
        multiple_color_names = []
        while count > 0:
            random_name_index = random.randint(0, len(color_names)-1)
            color_name = color_names.pop(random_name_index)
            multiple_color_names.append(color_name)
            count -= 1
        return multiple_color_names, [Utils.trim_string_end(name) for name in multiple_color_names]

    def fill_multiple_values_autocomplete(self, color_names: list) -> list:
        multiple_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_MULTIPLE, 'Get multiple colors autocomplete field')
        for name in color_names:
            multiple_colors_field.send_keys(name)
            multiple_colors_field.send_keys(Keys.RETURN)
        name_inputs = self.are_present('css', self.locators.MULTIPLE_COLOR_NAMES_INPUTS, 'Get multiple colors autocomplete field input values')
        return [input_name.text for input_name in name_inputs]

    def fill_single_values_autocomplete(self, color_names: list) -> str:
        single_colors_field = self.is_present('css', self.locators.AUTOCOMPLETE_SINGLE, 'Get single color autocomplete field')
        for name in color_names:
            single_colors_field.send_keys(name)
            single_colors_field.send_keys(Keys.RETURN)
        name_input = self.is_present('css', self.locators.SINGLE_COLOR_NAME_INPUT, 'Get single color autocomplete field input value')
        return name_input.text



