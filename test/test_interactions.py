import pytest
from pom.interactions_page import *


@pytest.mark.usefixtures('setup')
class TestInteractionsPage:
    def test_sortable(self):
        sortable_page = SortablePage(self.driver)
        sortable_page.open_page()
        initial_list_order, current_list_order = sortable_page.drag_sortable_item_in_list()
        assert current_list_order != initial_list_order, "Validating that sortable list is rearranged"

        initial_grid_order, current_grid__order = sortable_page.drag_sortable_item_in_grid()
        assert current_grid__order != initial_grid_order, "Validating that sortable grid is rearranged"

    def test_selectable(self):
        selectable_page = SelectablePage(self.driver)
        selectable_page.open_page()
        items_to_select, selected_items = selectable_page.select_items_in_list(3)
        assert selected_items == items_to_select, "Validating that correct items are selected in list"

        items_to_select, selected_items = selectable_page.select_items_in_grid(6)
        assert selected_items == items_to_select, "Validating that correct items are selected in grid"

    def test_resizable(self):
        MIN_BOX_SIZE = ["150", "150"]
        MAX_BOX_SIZE = ["500", "300"]
        INITIAL_OBJ_SIZE = ["200", "200"]
        resizable_page = ResizablePage(self.driver)
        resizable_page.open_page()
        max_size, min_size = resizable_page.change_resizable_box_size()
        assert max_size == MAX_BOX_SIZE and min_size == MIN_BOX_SIZE, "Validating that max and min clamps of resiable box"

        obj_size = resizable_page.change_resizable_object_size()
        assert obj_size != INITIAL_OBJ_SIZE, "Validating that size of resizable object is changed"