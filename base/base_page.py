import re
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException


class BasePage:
    def __init__(self, driver, url='https://demoqa.com/'):
        self.driver = driver
        self.url = url
        self.__wait = WebDriverWait(driver, 15, 1, ignored_exceptions=StaleElementReferenceException)

    def open_page(self):
        self.driver.get(self.url)

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
        return self.__wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_not_present(self, find_by: str, locator: str, locator_name=None) -> WebElement:  # check when it may be used
        return self.__wait.until(ec.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def is_clickable(self, find_by: str, locator: str, locator_name=None) -> WebElement:  # check when it may be used
        return self.__wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)), locator_name)

    def are_visible(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def are_present(self, find_by: str, locator: str, locator_name=None) -> list[WebElement]:
        return self.__wait.until(ec.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)),
                                 locator_name)

    def has_text(self, text: str) -> WebElement:
        return self.__wait.until(ec.presence_of_element_located((self.__get_selenium_by("xpath"), f"//*[text()='{text}']")))
    def get_text_from_webelements(self, elements: list[WebElement]) -> list[str]:
        return [element.text.lower() for element in elements]

    def go_to_element(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_element_by_text(self, elements: list[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]

    def select_from_element_by_text(self, locator: str, text: str):
        element = self.is_visible('css', locator, "Getting element to select from")
        Select(element).select_by_visible_text(text)

    def click_on_element_with_text(self, locator: str, value: str):
        elements = self.are_visible('css', locator, "Getting elements to select from")
        for element in elements:
            if element.text == value:
                element.click()
                break

    def delete_cookie(self, cookie_name: str) -> None:
        self.driver.delete_cookie(cookie_name)

    def action_doubleclick(self, element: WebElement) -> None:
        action = ActionChains(self.driver)
        action.double_click(element)
        action.perform()

    def action_right_click(self, element: WebElement) -> None:
        action = ActionChains(self.driver)
        action.context_click(element)
        action.perform()

    def switch_tab_by_handle(self, handle: int) -> None:
        self.driver.switch_to.window(self.driver.window_handles[handle])

    def drag_and_drop_to_location(self, element: WebElement, x_cord: int, y_cord: int):
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(element, x_cord, y_cord)
        action.perform()

    def drag_and_drop_to_element(self, element: WebElement, target_element: WebElement):
        action = ActionChains(self.driver)
        action.drag_and_drop(element, target_element)
        action.perform()

    def hold_move_release_element(self, element: WebElement, x_cord: int, y_cord: int):
        action = ActionChains(self.driver)
        action.click_and_hold(element)
        action.move_by_offset(x_cord, y_cord)
        action.release()
        action.perform()

    def drag_with_cursor(self, element, x_coord, y_coord):
        action = ActionBuilder(self.driver)
        action.pointer_action.click_and_hold(element)
        action.pointer_action.move_to_location(x_coord, y_coord)
        action.pointer_action.release()
        action.perform()

    def move_cursor_to_location(self, x_cord: int, y_cord: int):
        action = ActionBuilder(self.driver)
        action.pointer_action.move_to_location(x_cord, y_cord)
        action.perform()

    def move_to_element(self, element: WebElement):
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.pause(1)
        action.perform()

    def get_alert_text(self) -> str:
        alert = self.driver.switch_to.alert
        text = alert.text
        return text

    def get_element_size_attribute(self, element: WebElement) -> list:
        size = element.get_attribute('style')
        formatted_size = re.findall(r'\d+', size)
        return formatted_size

    def remove_footer(self):
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")
        self.driver.execute_script("document.getElementById('fixedban').remove();")

    def check_element_state_after_time(self, find_by: str, locator: str, condition: str, timeout: float = 10.0) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        if condition == 'visible':
            try:
                wait.until(ec.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(f'{error}\n Approximate elapsed time until element is visible is greater than {timeout} seconds')
                return False
        elif condition == 'present':
            try:
                wait.until(ec.presence_of_element_located((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(f'{error}\n Approximate elapsed time until element is present is greater than {timeout} seconds')
                return False
        elif condition == 'clickable':
            try:
                wait.until(ec.element_to_be_clickable((self.__get_selenium_by(find_by), locator)))
                return True
            except TimeoutException as error:
                print(
                    f'{error}\n Approximate elapsed time until element is clickable is greater than {timeout} seconds')
                return False
        else:
            return False

    def check_alert_is_present_after_time(self, timeout: float = 10.0) -> bool:
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.alert_is_present())
            return True
        except TimeoutException as error:
            print(f'{error}\n Approximate elapsed time until alert is present is more than {timeout} seconds')
            return False