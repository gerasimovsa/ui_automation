import collections

from base.base_page import BasePage
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePagePageLocators
import random
from selenium.webdriver.common.by import By
from base.utils import Utils


class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = TextBoxPageLocators()

    def fill_all_fields(self) -> [str]:
        person_info = next(generated_person())
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address
        self.is_visible('css', self.locators.FULL_NAME, 'Full name filed').send_keys(full_name)
        self.is_visible('css', self.locators.EMAIL, 'Email field').send_keys(email)
        self.is_visible('css', self.locators.CURRENT_ADDRESS, 'Current Address field').send_keys(current_address)
        self.is_visible('css', self.locators.PERMANENT_ADDRESS, 'Permanent Address field').send_keys(permanent_address)
        self.is_visible('css', self.locators.SUBMIT).click()
        return Utils.remove_newline([full_name, email, current_address, permanent_address])

    def get_output_forms_text(self) -> list[str]:
        full_name = self.is_present('css', self.locators.CREATED_FULL_NAME, 'Get Name output text').text.split(':')[1]
        email = self.is_present('css', self.locators.CREATED_EMAIL, 'Get Email output text').text.split(':')[1]
        current_address = \
            self.is_present('css', self.locators.CREATED_CURRENT_ADDRESS, 'Get Current Address output text').text.split(
                ':')[1]
        permanent_address = \
            self.is_present('css', self.locators.CREATED_PERMANENT_ADDRESS, 'Get Permanent Address text').text.split(
                ':')[1]
        return [full_name, email, current_address, permanent_address]


class CheckBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = CheckBoxPageLocators()

    def expand_checkbox_list(self) -> None:
        self.is_visible('css', self.locators.EXPAND_ALL_BUTTON, 'Expand hierarchy of checkboxes').click()

    def click_random_checkboxes(self):
        item_list = self.are_visible('css', self.locators.CHECKBOXES, 'Check random checkboxes')
        count = 15
        while count != 0:
            if count > 0:
                item = item_list[random.randint(1, 15)]
                self.go_to_element(item)
                item.click()
                count -= 1
            else:
                break

    def get_checked_checkboxes_text(self) -> list[str]:
        checked_list = self.are_present('css', self.locators.CHECKED_CHECKBOXES)
        checked_checkboxes_titles = []
        [checked_checkboxes_titles.append(checkbox.find_element(By.XPATH, self.locators.CHECKBOX_TITLE)) for checkbox in
         checked_list]
        checked_checkboxes_text = self.get_text_from_webelements(checked_checkboxes_titles)
        return Utils.format_checkbox_strings(checked_checkboxes_text)

    def get_output_results_text(self) -> list[str]:
        output_list = self.are_present('css', self.locators.OUTPUT_RESULTS)
        output_list_text = self.get_text_from_webelements(output_list)
        return Utils.format_checkbox_strings(output_list_text)


class RadioButtonPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = RadioButtonPageLocators()

    def get_active_rbs_text(self) -> list[str]:
        active_rbs = self.are_visible('css', self.locators.ACTIVE_RADIO_BUTTONS, 'Get active radio buttons text')
        return self.get_text_from_webelements(active_rbs)

    def get_output_after_rb_click(self) -> list[str]:
        active_rbs = self.are_visible('css', self.locators.ACTIVE_RADIO_BUTTONS, 'Get active radio buttons')
        output = []
        for rb in active_rbs:
            rb.click()
            current_output = self.is_present('css', self.locators.OUTPUT_RESULT, 'Get output text').text.lower()
            output.append(current_output)
        return output

        """""
        choices = {
            'yes': self.locators.YES_RADIO,
            'impressive': self.locators.IMPRESSIVE_RADIO,
            'no': self.locators.NO_RADIO
        }
        """""


class WebTablesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = WebTablePagePageLocators()

    def submit_registration_form(self, count: int = 5) -> list[str]:
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        while count != 0:
            self.is_visible('css', self.locators.ADD_BUTTON, 'Click on Add button').click()
            self.is_visible('css', self.locators.FIRSTNAME_INPUT).send_keys(first_name)
            self.is_visible('css', self.locators.LASTNAME_INPUT).send_keys(last_name)
            self.is_visible('css', self.locators.EMAIL_INPUT).send_keys(email)
            self.is_visible('css', self.locators.AGE_INPUT).send_keys(age)
            self.is_visible('css', self.locators.SALARY_INPUT).send_keys(salary)
            self.is_visible('css', self.locators.DEPARTMENT_INPUT).send_keys(department)
            self.is_visible('css', self.locators.SUBMIT, 'Click on Submit button').click()
            count -= 1
            return [first_name, last_name, str(age), email, str(salary), department]

    def get_table_entries(self):
        people_list = self.are_present('css', self.locators.TABLE_ROWS, "Getting entries from table")
        data = []
        for item in people_list:
            data.append(item.text.splitlines())
        return data

    def search_entry(self, search_by: str):
        self.is_present('css', self.locators.SEARCH_BOX, 'Entering into search box').send_keys(search_by)