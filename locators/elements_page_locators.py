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
    CHECKBOX_TITLE = (".//ancestor::span[@class='rct-text']")
    OUTPUT_RESULTS = "#result>span[class='text-success']"


class RadioButtonPageLocators:
    ACTIVE_RADIO_BUTTONS = "div>label[class='custom-control-label']"
    YES_RADIO = "label[for='yesRadio']"
    IMPRESSIVE_RADIO = "label[for='yesRadio']"
    NO_RADIO = "div>label[for='noRadio']"
    OUTPUT_RESULT = "span[class='text-success']"

