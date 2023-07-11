class AccordianPageLocators:
    FIRST_SECTION_TITLE = "div[id='section1Heading']"
    SECOND_SECTION_TITLE = "div[id='section2Heading']"
    THIRD_SECTION_TITLE = "div[id='section3Heading']"
    FIRST_SECTION_BODY = "div[id='section1Content']"
    SECOND_SECTION_BODY = "div[id='section2Content']"
    THIRD_SECTION_BODY = "div[id='section3Content']"


class AutoCompletePageLocators:
    AUTOCOMPLETE_MULTIPLE = "input[id='autoCompleteMultipleInput']"
    AUTOCOMPLETE_SINGLE = "input[id='autoCompleteSingleInput']"
    MULTIPLE_COLOR_NAMES_INPUTS = "div[class='css-12jo7m5 auto-complete__multi-value__label']"
    SINGLE_COLOR_NAME_INPUT = "div[class='auto-complete__single-value css-1uccc91-singleValue']"
    REMOVE_COLOR_NAME = "div[class='css-1rhbuit-multiValue auto-complete__multi-value'] svg path"