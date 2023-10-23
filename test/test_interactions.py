import pytest
import allure
from pom.interactions_page import *


@pytest.mark.usefixtures("setup_and_teardown")
@allure.suite("Interactions Page")
class TestInteractionsPage:
    @allure.feature("Sortable")
    class TestSortablePage:
        @allure.title("Sortable test")
        def test_sortable(self):
            sortable_page = SortablePage(self.driver)
            sortable_page.open_page()
            initial_list_order, current_list_order = sortable_page.drag_sortable_item_in_list()
            assert current_list_order != initial_list_order, "Validating that sortable list is rearranged"

            initial_grid_order, current_grid__order = sortable_page.drag_sortable_item_in_grid()
            assert current_grid__order != initial_grid_order, "Validating that sortable grid is rearranged"

    @allure.feature("Selectable")
    class TestSelectablePage:
        @allure.title("Selectable test")
        def test_selectable(self):
            selectable_page = SelectablePage(self.driver)
            selectable_page.open_page()
            items_to_select, selected_items = selectable_page.select_items_in_list(3)
            assert selected_items == items_to_select, "Validating that correct items are selected in list"

            items_to_select, selected_items = selectable_page.select_items_in_grid(6)
            assert selected_items == items_to_select, "Validating that correct items are selected in grid"

    @allure.feature("Resizable")
    class TestResizablePage:
        @allure.title("Resizable test")
        def test_resizable(self):
            MIN_BOX_SIZE = ["150", "150"]
            MAX_BOX_SIZE = ["500", "300"]
            INITIAL_OBJ_SIZE = ["200", "200"]
            resizable_page = ResizablePage(self.driver)
            resizable_page.open_page()
            max_size, min_size = resizable_page.change_resizable_box_size()
            assert max_size == MAX_BOX_SIZE and min_size == MIN_BOX_SIZE, \
                "Validating that max and min clamps of resiable box"

            obj_size = resizable_page.change_resizable_object_size()
            assert obj_size != INITIAL_OBJ_SIZE, "Validating that size of resizable object is changed"

    @allure.feature("Droppable")
    class TestDroppablePage:
        @allure.title("Droppable test")
        def test_droppable(self):
            RESULT_DROPPED = "Dropped!"
            RESULT_DROP_HERE = "Drop here"
            droppable_page = DroppablePage(self.driver)
            droppable_page.open_page()
            non_acceptable, acceptable = droppable_page.drag_on_accept_droppable()
            assert non_acceptable == RESULT_DROP_HERE, "Validating that droppable is not accepted"
            assert acceptable == RESULT_DROPPED, "Validating that droppable is accepted"

            simple_droppable = droppable_page.drag_on_simple_droppable()
            assert simple_droppable == RESULT_DROPPED, "Validating simple droppable"

            non_greedy, greedy = droppable_page.drag_on_propagated_droppable()
            assert non_greedy == (RESULT_DROPPED, RESULT_DROPPED) and greedy == ("Outer droppable", RESULT_DROPPED),\
                "Validating propagated droppable"

            is_reverted, is_preserved, result_text = droppable_page.drag_on_revert_droppable()
            assert is_reverted is True and is_preserved is True and result_text == RESULT_DROPPED, \
                "Validating preserve and revert droppable"

    @allure.feature("Draggable")
    class TestDraggablePage:
        @allure.title("Draggable test")
        def test_draggable(self):
            draggable_page = DraggablePage(self.driver)
            draggable_page.open_page()
            X_ONLY_INITIAL_LOC = (851, 407)
            Y_ONLY_INITIAL_LOC = (569, 407)
            MAX_BOT_RIGHT_BOX_LOC = (934, 510)
            MAX_BOT_RIGHT_TEXT_LOC = (441, 711)
            x_only_loc, y_only_loc = draggable_page.drag_axis_restricted_draggable()
            assert x_only_loc[0] == X_ONLY_INITIAL_LOC[0] and x_only_loc[1] != X_ONLY_INITIAL_LOC[1],\
                "Validating x restricted draggable"
            assert y_only_loc[0] != Y_ONLY_INITIAL_LOC[0] and y_only_loc[1] == Y_ONLY_INITIAL_LOC[1],\
                "Validating y restricted draggable"

            initial_loc, updated_loc = draggable_page.drag_simple_draggable()
            assert updated_loc != initial_loc, "Validating that box is dragged"

            box_loc, text_loc = draggable_page.drag_restricted_draggable()
            assert box_loc == MAX_BOT_RIGHT_BOX_LOC, "Validating that box is constrained"
            assert text_loc == MAX_BOT_RIGHT_TEXT_LOC, "Validating that text is constrained"

            y_axis_deviations = draggable_page.drag_cursor_style_draggable()
            print(y_axis_deviations)
            assert y_axis_deviations[0] in range(-10, 0), "Validating that center box has allowed deviation"
            assert y_axis_deviations[1] in range(0, 60), "Validating that center box has allowed deviation"
            assert y_axis_deviations[2] in range(-60, 0), "Validating that center box has allowed deviation"
