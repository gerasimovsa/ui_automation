import os
import calendar

from selenium.webdriver import Keys
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
from base.utils import Utils
from generator.generator import *
from locators.demoqa_urls import *
from locators.forms_page_locators import *


class PracticeFormPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = FormsPageUrls.PRACTICE_FORM
        self.locators = PracticeFormPageLocators()

    def submit_filled_form(self):
        states_and_cities = {
            "NCR": ["Delhi", "Gurgaon", "Noida"],
            "Uttar Pradesh": ["Agra", "Lucknow", "Merrut"],
            "Haryana": ["Karnal", "Panipat"],
            "Rajasthan": ["Jaipur", "Jaiselmer"]
        }
        random_month = str(random.randint(0, 11))
        random_year = str(random.randint(1990, 2004))
        random_state = list(states_and_cities.keys())[random.randint(0, 3)]
        cities_of_state = states_and_cities[random_state]
        random_city = cities_of_state[random.randint(0, len(cities_of_state) - 1)]
        person_info = next(generated_person())
        path = generate_file('text', 'png')
        subject = generate_autocomplete_subject()
        self.remove_footer()
        self.is_visible('css', self.locators.FIRST_NAME, 'First name filed').send_keys(person_info.first_name)
        self.is_visible('css', self.locators.LAST_NAME, 'Last name filed').send_keys(person_info.last_name)
        self.is_visible('css', self.locators.EMAIL, 'Email filed').send_keys(person_info.email)
        gender = self.is_visible('css', self.locators.RANDOM_GENDER_RADIO, 'Gender radio button').text
        self.is_visible('css', self.locators.RANDOM_GENDER_RADIO, 'Gender radio button').click()
        self.is_visible('css', self.locators.PHONE_NUMBER, 'Mobile field').send_keys(person_info.phone_number)

        date_of_birth_field = self.is_visible('css', self.locators.DATE_OF_BIRTH, 'Date of birth field')
        date_of_birth_field.click()
        year_dropdown = self.is_visible('css', self.locators.DATEPICKER_YEAR, 'Date year')
        Select(year_dropdown).select_by_value(random_year)
        month_dropdown = self.is_visible('css', self.locators.DATEPICKER_MONTH, 'Date month')
        Select(month_dropdown).select_by_value(random_month)
        days = self.are_visible('xpath', self.locators.DATEPICKER_DAY, 'Date day')
        days[random.randint(0, len(days) - 1)].click()
        date_of_birth = date_of_birth_field.get_attribute("value").lower()
        short_month = calendar.month_abbr[int(random_month)+1].lower()
        full_month = calendar.month_name[int(random_month)+1].lower()
        date_with_full_month = date_of_birth.replace(short_month, full_month)

        self.is_visible('css', self.locators.SUBJECT, 'Subject field').send_keys(subject)
        self.is_visible('css', self.locators.SUBJECT, 'Subject field').send_keys(Keys.RETURN)
        self.is_visible('css', self.locators.RANDOM_HOBBY_CHECKBOX, 'Hobby checkboxes').click()
        hobby = self.is_visible('css', self.locators.RANDOM_HOBBY_CHECKBOX, 'Hobby checkboxes').text
        upload_button = self.is_present('css', self.locators.UPLOAD_PICTURE, 'Upload picture')
        upload_button.send_keys(path)
        filename = os.path.basename(path)
        self.is_visible('css', self.locators.CURRENT_ADDRESS, 'Address field').send_keys(person_info.current_address)
        states_dropdown = self.is_present('css', self.locators.STATE_DROPDOWN, 'State dropdown')
        self.go_to_element(states_dropdown)
        self.is_visible('css', self.locators.STATE_INPUT, 'State input').send_keys(random_state)
        self.is_visible('css', self.locators.STATE_INPUT, 'State input').send_keys(Keys.RETURN)
        self.is_visible('css', self.locators.CITY_INPUT, 'City input').send_keys(random_city)
        self.is_visible('css', self.locators.CITY_INPUT, 'City input').send_keys(Keys.RETURN)
        submit_button = self.is_visible('css', self.locators.SUBMIT, 'Submit button')
        self.go_to_element(submit_button)
        submit_button.click()
        os.remove(path)
        input_data = [f"{person_info.first_name} {person_info.last_name}",
                      person_info.email,
                      gender,
                      person_info.phone_number[:10],
                      date_with_full_month,
                      subject,
                      hobby,
                      filename,
                      person_info.current_address.replace('\n', ' ').replace(',', ' '),
                      f"{random_state} {random_city}"]
        return [string.lower() for string in input_data]

    def get_table_data(self):
        data = []
        locators = self.locators.TABLE_DATA_LOCATORS
        for locator in locators:
            field_text = self.is_visible('xpath', locator, 'Table field').text.replace(',', ' ').lower()
            data.append(field_text)
        self.is_visible('css', self.locators.CLOSE_BUTTON, 'Close button').click()
        return Utils.remove_newline(data)

