from base.base_page import BasePage
from locators.elements_page_locators import TextBoxPageLocators


class TextBoxPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.is_visible('css', self.locators.EMAIL, 'Full name filed').send_keys('yeah')
        self.is_visible('css', self.locators.EMAIL, 'Email field').send_keys('yeah@boy.com')
        self.is_visible('css', self.locators.CURRENT_ADDRESS, 'Current Address field').send_keys('gay_street')
        self.is_visible('css', self.locators.PERMANENT_ADDRESS, 'Permanent Address field').send_keys('lesbian_driveway')
        self.is_visible('css', self.locators.SUBMIT).click()
