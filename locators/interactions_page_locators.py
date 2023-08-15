
class SortablePageLocators:
    LIST_TAB = "a[id='demo-tab-list']"
    LIST_ITEMS = "div[id='demo-tabpane-list'] div[class='list-group-item list-group-item-action']"

    GRID_TAB = "a[id='demo-tab-grid']"
    GRID_ITEMS = "div[id='demo-tabpane-grid'] div[class='list-group-item list-group-item-action']"


class SelectablePageLocators:
    LIST_ITEMS = "div[id='demo-tabpane-list'] li"
    SELECTED_LIST_ITEMS = "li[class='mt-2 list-group-item active list-group-item-action']"

    GRID_TAB = "a[id='demo-tab-grid']"
    GRID_ITEMS = "div[id='demo-tabpane-grid'] li"
    SELECTED_GRID_ITEMS = "li[class='list-group-item active list-group-item-action']"


