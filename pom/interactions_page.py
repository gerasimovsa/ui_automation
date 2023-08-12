import random

from base.base_page import BasePage
from base.utils import Utils
from locators.interactions_page_locators import *
from locators.demoqa_urls import InteractionsPageUrls


class SortablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.SORTABLE
        self.locators = SortablePageLocators()

    def drag_sortable_item_in_list(self):
        sortable_list_items = self.are_visible('css', self.locators.LIST_ITEMS, "Getting sortable list items")
        initial_order = self.get_text_from_webelements(sortable_list_items)
        random_items = random.sample(sortable_list_items, k=2)
        to_move_item, target_item = random_items[0], random_items[1]
        self.drag_and_drop_to_element(to_move_item, target_item)
        current_order = self.get_text_from_webelements(self.are_visible('css', self.locators.LIST_ITEMS, ""))
        return initial_order, current_order

    def drag_sortable_item_in_grid(self):
        grid_tab_button = self.is_visible('css', self.locators.GRID_TAB, "Clicking or grid button")
        grid_tab_button.click()
        sortable_grid_items = self.are_visible('css', self.locators.GRID_ITEMS, "Getting sortable grid items")
        initial_order = self.get_text_from_webelements(sortable_grid_items)
        random_items = random.sample(sortable_grid_items, k=2)
        to_move_item, target_item = random_items[0], random_items[1]
        self.drag_and_drop_to_element(to_move_item, target_item)
        current_order = self.get_text_from_webelements(self.are_visible('css', self.locators.GRID_ITEMS, ""))
        return initial_order, current_order
