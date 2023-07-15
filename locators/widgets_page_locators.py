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


class DatePickerLocators:
    DATE_FIELD = "input[id='datePickerMonthYearInput']"
    DATE_SELECT_MONTH = "select[class='react-datepicker__month-select']"
    DATE_SELECT_YEAR = "select[class='react-datepicker__year-select']"
    DATE_SELECT_DAY_LIST = "div[class*='react-datepicker__day react-datepicker__day']"

    DATETIME_FIELD = "input[id='dateAndTimePickerInput']"
    DATETIME_SELECT_MONTH = "div[class='react-datepicker__month-read-view']"
    DATETIME_SELECT_YEAR = "div[class='react-datepicker__year-read-view']"
    DATETIME_SELECT_YEAR_LIST = "div[class*='react-datepicker__year-option']"
    DATETIME_SELECT_MONTH_LIST = "div[class*='react-datepicker__month-option']"
    DATETIME_SELECT_DAY_LIST = "div[class*='react-datepicker__day react-datepicker__day']"
    DATETIME_SELECT_TIME_LIST = "li[class*='react-datepicker__time-list-item']"
    YEAR_SCROLL_DOWN = "a[class='react-datepicker__navigation react-datepicker__navigation--years react-datepicker__navigation--years-previous']"