from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium.common.exceptions import StaleElementReferenceException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)

    def __get_selenium_by(self, find_by: str) -> str:
        find_by = find_by.lower()
        locators = {
            'css': By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'id': By.ID,
            'name': By.NAME,
            'tag': By.TAG_NAME,
            'partial_link': By.PARTIAL_LINK_TEXT,
            'link': By.LINK_TEXT,
            'class': By.CLASS_NAME
        }
        return locators[find_by]

    def is_visible(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name: object = None) -> List[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_present(self, find_by: str, locator: str, locator_name=None) -> List[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)

    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
       return [element.text for element in elements]

    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)
