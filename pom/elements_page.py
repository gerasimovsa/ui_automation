from base.base_page import BasePage
from generator.generator import generated_person
from locators.elements_page_locators import TextBoxPageLocators

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
        return [full_name, email, current_address.replace("\n", " "), permanent_address.replace("\n", " ")]

    def get_output_forms_text(self) -> [str]:
        full_name = self.is_present('css', self.locators.CREATED_FULL_NAME, 'Get Name output text').text.split(':')[1]
        email = self.is_present('css', self.locators.CREATED_EMAIL, 'Get Email output text').text.split(':')[1]
        current_address = self.is_present('css', self.locators.CREATED_CURRENT_ADDRESS, 'Get Current Address output text').text.split(':')[1]
        permanent_address = self.is_present('css', self.locators.CREATED_PERMANENT_ADDRESS, 'Get Permanent Address text').text.split(':')[1]
        return [full_name, email, current_address, permanent_address]
