from selenium.webdriver.support.events import AbstractEventListener
from base.base_page import BasePage


class ClickListener(AbstractEventListener):

    def before_click(self, element, driver):
        BasePage(driver).delete_cookie('ak_bmsc')

    def after_click(self, element, driver):
        BasePage(driver).delete_cookie('ak_bmsc')
