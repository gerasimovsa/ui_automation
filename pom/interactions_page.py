import random
import re
import numpy
import time

from selenium.webdriver.remote.webelement import WebElement

from base.base_page import BasePage
from locators.demoqa_urls import InteractionsPageUrls
from locators.interactions_page_locators import *


class SortablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.SORTABLE
        self.locators = SortablePageLocators()

    def drag_sortable_item_in_list(self) -> list:
        sortable_list_items = self.are_visible('css', self.locators.LIST_ITEMS, "Getting sortable list items")
        initial_order = self.get_text_from_webelements(sortable_list_items)
        random_items = random.sample(sortable_list_items, k=2)
        to_move_item, target_item = random_items[0], random_items[1]
        self.drag_and_drop_to_element(to_move_item, target_item)
        current_order = self.get_text_from_webelements(self.are_visible('css', self.locators.LIST_ITEMS, ""))
        return initial_order, current_order

    def drag_sortable_item_in_grid(self) -> list:
        grid_tab_button = self.is_visible('css', self.locators.GRID_TAB, "Clicking or grid button")
        grid_tab_button.click()
        sortable_grid_items = self.are_visible('css', self.locators.GRID_ITEMS, "Getting sortable grid items")
        initial_order = self.get_text_from_webelements(sortable_grid_items)
        random_items = random.sample(sortable_grid_items, k=2)
        to_move_item, target_item = random_items[0], random_items[1]
        self.drag_and_drop_to_element(to_move_item, target_item)
        current_order = self.get_text_from_webelements(self.are_visible('css', self.locators.GRID_ITEMS, ""))
        return initial_order, current_order


class SelectablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.SELECTABLE
        self.locators = SelectablePageLocators()

    def select_items_in_list(self,
                             items_count: int) -> list:  # Convert this and following function into a single function with condition later
        if items_count > 5 or items_count < 1:
            items_count = random.randint(1, 4)
        select_list_items = self.are_visible('css', self.locators.LIST_ITEMS, "Getting selectable list items")
        random_items = random.sample(select_list_items, k=items_count)
        for item in random_items:
            item.click()
        selected_items = self.are_present('css', self.locators.SELECTED_LIST_ITEMS, "Getting selected items")
        return [item.text for item in random_items].sort(), [item.text for item in selected_items].sort()

    def select_items_in_grid(self, items_count: int) -> str:
        self.is_visible('css', self.locators.GRID_TAB, "Switching to grid tab").click()
        if items_count > 9 or items_count < 1:
            items_count = random.randint(1, 9)
        select_list_items = self.are_visible('css', self.locators.GRID_ITEMS, "Getting selectable grid items")
        random_items = random.sample(select_list_items, k=items_count)
        for item in random_items:
            item.click()
        selected_items = self.are_present('css', self.locators.SELECTED_GRID_ITEMS, "Getting selected items")
        return [item.text for item in random_items].sort(), [item.text for item in selected_items].sort()


class ResizablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.RESIZABLE
        self.locators = DroppablePageLocators()

    def get_element_size_attribute(self, element: WebElement) -> list:
        size = element.get_attribute('style')
        formatted_size = re.findall(r'\d+', size)
        return formatted_size

    def change_resizable_box_size(self):
        box = self.is_visible('css', self.locators.RESIZABLE_BOX, "Get resizable box")
        box_handle = self.is_clickable('xpath', self.locators.RESIZABLE_BOX_HANDLE, "Getting resizable box handle")
        self.drag_and_drop_to_location(box_handle, 400, 150)
        max_size = self.get_element_size_attribute(box)
        self.drag_and_drop_to_location(box_handle, -400, -150)
        min_size = self.get_element_size_attribute(box)
        return max_size, min_size

    def change_resizable_object_size(self):
        obj = self.is_visible('css', self.locators.RESIZABLE_OBJECT, "Get resizable object")
        object_handle = self.is_clickable('xpath', self.locators.RESIZABLE_OBJECT_HANDLE,
                                          "Getting resizable object handle")
        self.go_to_element(object_handle)
        random_coords = [random.randint(100, 200), random.randint(100, 200)]
        self.drag_and_drop_to_location(object_handle, random_coords[0], random_coords[1])
        size = self.get_element_size_attribute(obj)
        return size


class DroppablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.DROPPABLE
        self.locators = DroppablePageLocators()

    def drag_on_accept_droppable(self):
        self.is_visible("css", self.locators.ACCEPT_TAB, "Switching to Accept tab").click()
        accept = self.is_visible("css", self.locators.ACCEPTABLE, "Getting accept draggable")
        non_accept = self.is_visible("css", self.locators.NOT_ACCEPTABLE, "Getting not accept draggable")
        accept_box = self.is_visible("css", self.locators.ACCEPT_BOX, "Getting accept dropbox")
        self.drag_and_drop_to_element(non_accept, accept_box)
        non_accept_result = accept_box.text
        self.drag_and_drop_to_element(accept, accept_box)
        accept_result = accept_box.text
        return non_accept_result, accept_result

    def drag_on_simple_droppable(self):
        self.is_visible("css", self.locators.SIMPLE_TAB, "Switching to Simple tab").click()
        simple_draggable = self.is_visible("css", self.locators.SIMPLE_DRAGGABLE, "Getting simple draggable")
        simple_droppable = self.is_visible("css", self.locators.SIMPLE_DROPPABLE, "Getting simple droppable")
        self.drag_and_drop_to_element(simple_draggable, simple_droppable)
        simple_result = simple_droppable.text
        return simple_result

    def drag_on_propagated_droppable(self):
        self.is_visible("css", self.locators.PREVENT_TAB, "Switching to Prevent Propagation tab").click()
        drag_box = self.is_visible("css", self.locators.DRAG_BOX, "Getting drag box")
        outer_non_greedy = self.is_visible("css", self.locators.NON_GREEDY_OUTER, "Getting outer non-greedy")
        outer_greedy = self.is_visible("css", self.locators.GREEDY_OUTER, "Getting outer greedy")
        inner_non_greedy = self.is_visible("css", self.locators.NON_GREEDY_INNER, "Getting inner non-greedy")
        inner_greedy = self.is_visible("css", self.locators.GREEDY_INNER, "Getting inner greedy")

        self.drag_and_drop_to_element(drag_box, inner_non_greedy)
        non_greedy_outer_text = outer_non_greedy.text
        non_greedy_inner_text = inner_non_greedy.text
        non_greedy_result = (non_greedy_outer_text, non_greedy_inner_text)

        self.go_to_element(inner_greedy)
        self.drag_and_drop_to_element(drag_box, inner_greedy)
        greedy_outer_text = outer_greedy.text
        greedy_inner_text = inner_greedy.text
        greedy_result = (greedy_outer_text, greedy_inner_text)
        return non_greedy_result, greedy_result

    def drag_on_revert_droppable(self):
        self.is_visible("css", self.locators.REVERT_TAB, "Switching to Revert tab").click()
        revert_droppable = self.is_visible("css", self.locators.REVERT_DROPPABLE, "Getting revert droppable")

        revert_draggable = self.is_visible("css", self.locators.REVERT_BOX, "Getting revert drag box")
        initial_draggable_location = revert_draggable.location
        self.drag_and_drop_to_element(revert_draggable, revert_droppable)
        time.sleep(1)
        after_drag_revert_location = revert_draggable.location
        is_reverted = after_drag_revert_location == initial_draggable_location

        non_revert_draggable = self.is_visible("css", self.locators.NON_REVERT_BOX, "Getting non-revert drag box")
        self.drag_and_drop_to_element(non_revert_draggable, revert_droppable)
        time.sleep(1)
        after_drag_non_revert_location = non_revert_draggable.location
        is_preserved = after_drag_non_revert_location != initial_draggable_location
        return is_reverted, is_preserved, revert_droppable.text


class DraggablePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.url = InteractionsPageUrls.DRAGGABLE
        self.locators = DraggablePageLocators()

    def drag_axis_restricted_draggable(self):
        self.is_visible('css', self.locators.AXIS_RESTRICTED_TAB, "Switching tab").click()
        x_draggable = self.is_visible('css', self.locators.DRAG_BOX_ONLY_X, "Getting only x draggable")
        y_draggable = self.is_visible('css', self.locators.DRAG_BOX_ONLY_Y, "Getting only y draggable")

        random_offset_x = random.randint(100, 200)
        random_offset_y = random.randint(100, 200)
        self.drag_and_drop_to_location(x_draggable, random_offset_x, random_offset_y)
        self.drag_and_drop_to_location(y_draggable, random_offset_x, random_offset_y)
        updated_x_draggable_location = tuple(x_draggable.location.values())
        updated_y_draggable_location = tuple(y_draggable.location.values())
        return updated_x_draggable_location, updated_y_draggable_location

    def drag_simple_draggable(self):
        self.is_visible('css', self.locators.SIMPLE_TAB, "Switching tab").click()
        drag_box = self.is_visible('css', self.locators.DRAG_BOX, "Getting draggable")
        initial_drag_box_loc = tuple(drag_box.location.values())
        random_offset_x = random.randint(100, 300)
        random_offset_y = random.randint(100, 300)
        self.drag_and_drop_to_location(drag_box, random_offset_x, random_offset_y)
        updated_drag_box_loc = tuple(drag_box.location.values())
        return initial_drag_box_loc, updated_drag_box_loc

    def drag_restricted_draggable(self):
        self.is_visible('css', self.locators.CONTAINER_RESTRICTED_TAB, "Switching tab").click()
        r_box = self.is_visible('css', self.locators.RESTRICTED_BOX, "Get restricted box")
        r_text = self.is_visible('css', self.locators.RESTRICTED_TEXT, "Get restricted text")
        self.drag_with_cursor(r_box, 1050, 650)
        box_bot_right_clamp = tuple(r_box.location.values())
        self.go_to_element(r_text)
        self.drag_with_cursor(r_text, 1000, 500)
        text_bot_right_clamp = tuple(r_text.location.values())
        return box_bot_right_clamp, text_bot_right_clamp

    def drag_cursor_style_draggable(self):
        self.is_visible('css', self.locators.CURSOR_STYLE_TAB, "Switching tab").click()
        box_center = self.is_visible('css', self.locators.CURSOR_CENTER, "Getting center cursor")
        box_top_left = self.is_visible('css', self.locators.CURSOR_TOP_LEFT, "Getting top left cursor")
        box_bottom = self.is_visible('css', self.locators.CURSOR_BOTTOM, "Getting bottom cursor")
        draggable_boxes = [box_center, box_top_left, box_bottom]
        diffs = []
        for box in draggable_boxes:
            initial_loc = tuple(box.location.values())
            self.drag_and_drop_to_location(box, 200, 0)
            updated_loc = tuple(box.location.values())
            diff = numpy.subtract(updated_loc, initial_loc)
            diffs.append(diff[1])
        return diffs
