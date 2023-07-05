class BrowserWindowsPageLocators:
    NEW_TAB_BUTTON = "button[id='tabButton']"
    NEW_WINDOW_BUTTON = "button[id='windowButton']"
    NEW_WINDOW_MESSAGE = "button[id='messageWindowButton']"
    NEW_WINDOW_HEADER = "h1[id='sampleHeading']"


class AlertsPageLocators:
    ALERT_BUTTON = "button[id='alertButton']"
    TIMER_ALERT_BUTTON = "button[id='timerAlertButton']"
    CONFIRM_BUTTON = "button[id='confirmButton']"
    CONFIRM_RESULT = "span[id='confirmResult']"
    PROMPT_BUTTON = "button[id='promtButton']"
    PROMPT_RESULT = "span[id='promptResult']"


class FramesPageLocators:
    FRAME_1 = "iframe[id='frame1']"
    FRAME_2 = "iframe[id='frame2']"
    TITLE_FRAME = "h1[id='sampleHeading']"


class NestedFramesPageLocators:
    PARENT_FRAME = "iframe[id='frame1']"
    CHILD_FRAME = "iframe[srcdoc='<p>Child Iframe</p>']"
    PARENT_FRAME_TEXT = "body"
    CHILD_FRAME_TEXT = "p"


class ModalDialogsPageLocators:
    SMALL_MODAL_BUTTON = "button[id='showSmallModal']"
    SMALL_MODAL_CLOSE_BUTTON = "button[id='closeSmallModal']"
    BODY_SMALL_MODAL = "div[class='modal-body']"
    TITLE_SMALL_MODAL = "div[id='example-modal-sizes-title-sm']"

    LARGE_MODAL_BUTTON = "button[id='showLargeModal']"
    LARGE_MODAL_CLOSE_BUTTON = "button[id='closeLargeModal']"
    BODY_LARGE_MODAL = "div[class='modal-body']>p"
    TITLE_LARGE_MODAL = "div[id='example-modal-sizes-title-lg']"