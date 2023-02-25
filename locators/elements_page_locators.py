class TextBoxPageLocators:
    # forms
    FULL_NAME = "input[id='userName']"
    EMAIL = "input[id='userEmail']"
    CURRENT_ADDRESS = "textarea[id='currentAddress']"
    PERMANENT_ADDRESS = "textarea[id='permanentAddress']"
    SUBMIT = "button[id='submit']"
    # created form
    CREATED_FULL_NAME = "#output #name"
    CREATED_EMAIL = "#output #email"
    CREATED_CURRENT_ADDRESS = "#output #currentAddress"
    CREATED_PERMANENT_ADDRESS = "#output #permanentAddress"


class CheckBoxPageLocators:
    EXPAND_ALL_BUTTON = "button[title='Expand all']"
    COLLAPSE_ALL_BUTTON = "button[title='Collapse all']"
    CHECKBOXES = "span[class = 'rct-title']"
    CHECKED_CHECKBOXES = "svg[class='rct-icon rct-icon-check']"
    CHECKBOX_TITLE = ".//ancestor::span[@class='rct-text']"
    OUTPUT_RESULTS = "#result>span[class='text-success']"


class RadioButtonPageLocators:
    ACTIVE_RADIO_BUTTONS = "div>label[class='custom-control-label']"
    YES_RADIO = "label[for='yesRadio']"
    IMPRESSIVE_RADIO = "label[for='yesRadio']"
    NO_RADIO = "div>label[for='noRadio']"
    OUTPUT_RESULT = "span[class='text-success']"


class WebTablePagePageLocators:
    ADD_BUTTON = "button[id='addNewRecordButton']"
    FIRSTNAME_INPUT = "input[id='firstName']"
    LASTNAME_INPUT = "input[id='lastName']"
    EMAIL_INPUT = "input[id='userEmail']"
    AGE_INPUT = "input[id='age']"
    SALARY_INPUT = "input[id='salary']"
    DEPARTMENT_INPUT = "input[id='department']"
    SUBMIT = "button[id='submit']"
    TABLE_ROWS = "div[class='rt-tr-group']"
    SEARCH_BOX = "input[id='searchBox']"
    DELETE_BUTTONS = "span[title='Delete']"
    ROW_PARENT = ".//ancestor::div[@class='rt-tr-group']"
    EDIT_BUTTON = "span[title='Edit']"
    NO_ROWS_FOUND = "div[class='rt-noData']"
    ROWS_DROPDOWN = "select[aria-label='rows per page']"


class ButtonsPageLocators:
    DOUBLE_CLICK_BUTTON = "button[id='doubleClickBtn']"
    RIGHT_CLICK_BUTTON = "button[id='rightClickBtn']"
    CLICK_ME_BUTTON = "//button[text() = 'Click Me']"
    DOUBLE_CLICK_SUCCESS = "p[id='doubleClickMessage']"
    RIGHT_CLICK_SUCCESS = "p[id='rightClickMessage']"
    CLICK_ME_SUCCESS = "p[id='dynamicClickMessage']"
