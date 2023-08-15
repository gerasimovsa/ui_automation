import time

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
