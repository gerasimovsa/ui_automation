import time
import requests as r
import re
from base.base_page import BasePage
from generator.generator import generated_person
from locators.elements_page_locators import *
import random
from base.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


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


class WebTablesPage(BasePage):  # store CONSTANT expected results here
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

    def fill_search_field(self, keyword: str):
        self.is_visible('css', self.locators.SEARCH_BOX, 'Entering into search box').send_keys(keyword)

    def get_raw_text_by_delete_button(self):
        delete_button = self.is_present('css', self.locators.DELETE_BUTTONS, 'Find all rows with delete buttons')
        row = delete_button.find_element(By.XPATH, self.locators.ROW_PARENT)
        return row.text.splitlines()

    def edit_table_entry(self) -> str:
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        email = person_info.email
        age = person_info.age
        salary = person_info.salary
        department = person_info.department
        input_fields_list = [
            self.locators.FIRSTNAME_INPUT,
            self.locators.LASTNAME_INPUT,
            self.locators.EMAIL_INPUT,
            self.locators.AGE_INPUT,
            self.locators.SALARY_INPUT,
            self.locators.DEPARTMENT_INPUT]
        person_info_list = [first_name, last_name, email, age, salary, department]
        random_index = random.randint(0, 5)
        self.is_visible('css', self.locators.EDIT_BUTTON, 'Clicking on Edit button').click()
        random_field = self.is_visible('css', input_fields_list[random_index], 'Getting random field')
        random_field.clear()
        random_field.send_keys(person_info_list[random_index])
        self.is_visible('css', self.locators.SUBMIT, 'Click on Submit button').click()
        return person_info_list[random_index]

    def delete_table_entry(self) -> str:
        self.is_visible('css', self.locators.DELETE_BUTTONS, 'Clicking on Delete button').click()
        return self.is_present('css', self.locators.NO_ROWS_FOUND, 'No rows found message').text

    def get_rows_count(self) -> int:
        table_rows = self.are_present('css', self.locators.TABLE_ROWS, 'Getting table rows')
        return len(table_rows)

    def select_from_rows_dropdown(self) -> list[int]:
        rows_numbers = [5, 10, 20]
        data = []
        for number in rows_numbers:
            rows_dropdown = self.is_visible('css', self.locators.ROWS_DROPDOWN, 'Getting rows dropdown')
            self.go_to_element(rows_dropdown)
            rows_dropdown.click()
            Select(rows_dropdown).select_by_value(str(number))
            data.append(self.get_rows_count())
        return data


class ButtonsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = ButtonsPageLocators()
        self.BUTTONS = ['double', 'right', 'click']
        self.SUCCESS_CLICK_TEXT = ['You have done a double click', 'You have done a right click',
                                   'You have done a dynamic click']

    def click_on_each_button(self, click_type: str) -> str:
        if click_type == 'double':
            self.action_doubleclick(
                self.is_visible('css', self.locators.DOUBLE_CLICK_BUTTON, 'Getting doubleclick button'))
            success = self.is_present('css', self.locators.DOUBLE_CLICK_SUCCESS, 'Getting doubleclick success')
            return success.text
        if click_type == 'right':
            self.action_right_click(
                self.is_visible('css', self.locators.RIGHT_CLICK_BUTTON, 'Getting right click button'))
            success = self.is_present('css', self.locators.RIGHT_CLICK_SUCCESS, 'Getting right click success')
            return success.text
        if click_type == 'click':
            self.is_visible('xpath', self.locators.CLICK_ME_BUTTON, 'Getting dynamic click button').click()
            self.action_right_click(
                self.is_visible('css', self.locators.RIGHT_CLICK_BUTTON, 'Getting right click button'))
            success = self.is_present('css', self.locators.CLICK_ME_SUCCESS, 'Getting dynamic click success')
            return success.text


class LinksPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.locators = LinksPageLocators()
        self.API_CALL_URLS = [
            'created',
            'no-content',
            'moved',
            'bad-request',
            'unauthorized',
            'forbidden',
            'invalid-url'
        ]

    def check_home_link(self) -> str:
        home_link = self.is_visible('css', self.locators.HOME_LINK, 'Getting home link')
        home_link_href = home_link.get_attribute("href")
        response = r.get('home_link_href')
        if response.status_code == 200:
            home_link.click()
            self.switch_tab_by_handle(1)
            current_url = self.driver.current_url
            return home_link_href, current_url
        else:
            return f'Invalid status code. Response status code: {response.status_code}. Link href: {home_link_href}'

    def check_api_call_links(self) -> list[str]:
        api_call_locators = self.locators.API_CALL_LINKS
        api_call_links = [self.is_visible('css', link_locator) for link_locator in api_call_locators]
        status_codes = []
        messages = []
        for api_call_link in api_call_links:
            api_call_link.click()
            time.sleep(1)
            response_text = self.is_present('css', self.locators.LINK_RESPONSE, 'Getting response text').text
            response_statuscode = re.search(r'\d+', response_text).group()
            message = response_text[50:].replace(' Permanently', '').lower()

            status_codes.append(response_statuscode)
            messages.append(message)
        return status_codes, messages

    def send_calls_get_status_code(self) -> list[str]:
        api_call_urls = [f'https://demoqa.com/{link}' for link in self.API_CALL_URLS]
        response_codes = []
        for url in api_call_urls:
            response = r.get(url)
            response_codes.append(str(response.status_code))
        return response_codes

    def get_api_call_links_text(self) -> list[str]:
        api_call_locators = self.locators.API_CALL_LINKS
        api_call_links = [self.is_visible('css', link_locator) for link_locator in api_call_locators]
        api_call_links_text = self.get_text_from_webelements(api_call_links)
        return api_call_links_text

