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
