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


class ResizablePageLocators:
    RESIZABLE_BOX = "div[id='resizableBoxWithRestriction']"
    RESIZABLE_BOX_HANDLE = "//*[@id='resizableBoxWithRestriction']/span"

    RESIZABLE_OBJECT = "div[id='resizable']"
    RESIZABLE_OBJECT_HANDLE = "//*[@id='resizable']/span"


class DroppablePageLocators:
    SIMPLE_TAB = "a[id='droppableExample-tab-simple']"
    SIMPLE_DRAGGABLE = "div[id='draggable']"
    SIMPLE_DROPPABLE = "#simpleDropContainer #droppable"

    ACCEPT_TAB = "a[id='droppableExample-tab-accept']"
    ACCEPTABLE = "div[id='acceptable']"
    NOT_ACCEPTABLE = "div[id='notAcceptable']"
    ACCEPT_BOX = "#droppableExample-tabpane-accept #droppable"

    PREVENT_TAB = "a[id='droppableExample-tab-preventPropogation']"
    DRAG_BOX = "div[id='dragBox']"
    NON_GREEDY_OUTER = "div[id='notGreedyDropBox']>p"
    NON_GREEDY_INNER = "div[id='notGreedyInnerDropBox']>p"
    GREEDY_OUTER = "div[id='greedyDropBox']>p"
    GREEDY_INNER = "div[id='greedyDropBoxInner']>p"

    REVERT_TAB = "a[id='droppableExample-tab-revertable']"
    REVERT_BOX = "div[id='revertable']"
    NON_REVERT_BOX = "div[id='notRevertable']"
    REVERT_DROPPABLE = "#revertableDropContainer #droppable"


class DraggablePageLocators:
    SIMPLE_TAB = "a[id='draggableExample-tab-simple']"
    DRAG_BOX = "div[id='dragBox']"

    AXIS_RESTRICTED_TAB = "a[id='draggableExample-tab-axisRestriction']"
    DRAG_BOX_ONLY_Y = "div[id='restrictedX']"
    DRAG_BOX_ONLY_X = "div[id='restrictedY']"

    CONTAINER_RESTRICTED_TAB = "a[id='draggableExample-tab-containerRestriction']"
    RESTRICTIVE_CONTAINER = "div[id='containmentWrapper']"
    RESTRICTED_BOX = "div[id='containmentWrapper']>div"
    RESTRICTIVE_WIDGET = "div[class='draggable ui-widget-content m-3']"
    RESTRICTED_TEXT = "div[class='draggable ui-widget-content m-3']>span"

    CURSOR_STYLE_TAB = "a[id='draggableExample-tab-cursorStyle']"
    CURSOR_CENTER = "div[id='cursorCenter']"
    CURSOR_TOP_LEFT = "div[id='cursorTopLeft']"
    CURSOR_BOTTOM = "div[id='cursorBottom']"
