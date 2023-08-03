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


class SliderLocators:
    SLIDER = "input[class='range-slider range-slider--primary']"
    SLIDER_FIELD = "input[id='sliderValue']"


class ProgressBarLocators:
    PROGRESS_BAR = "div[id='progressBar']>div"
    START_STOP_BUTTON = "button[id='startStopButton']"
    RESET_BUTTON = "button[id='resetButton']"


class TabsLocators:
    FIRST_TAB_TITLE = "a[id='demo-tab-what']"
    SECOND_TAB_TITLE = "a[id='demo-tab-origin']"
    THIRD_TAB_TITLE = "a[id='demo-tab-use']"
    FIRST_TAB_BODY = "div[id='demo-tabpane-what']>p"
    SECOND_TAB_BODY = "div[id='demo-tabpane-origin']>p[class]"
    THIRD_TAB_BODY = "div[id='demo-tabpane-use']>p"


class TooltipsLocators:
    HOVER_BUTTON = "//*[@id='toolTipButton']"
    TOOLTIP_BUTTON = "button[aria-describedby='buttonToolTip']"

    HOVER_FIELD = "//*[@id='toolTipTextField']"
    TOOLTIP_FIELD = "input[aria-describedby='textFieldToolTip']"

    HOVER_LINK_TEXT = "//*[.='Contrary']"
    TOOLTIP_LINK_TEXT = "a[aria-describedby='contraryTexToolTip']"

    HOVER_LINK_NUMBERS = "//*[.='1.10.32']"
    TOOLTIP_LINK_NUMBERS = "a[aria-describedby='sectionToolTip']"

    ACTIVE_TOOLTIP = "div[class='tooltip-inner']"


class MenuLocators:
    MENU_ITEMS = "ul[id='nav'] li a"


class SelectMenuLocators:
    SELECT_VALUE_DROPDOWN = "input[id='react-select-2-input']"
    SELECT_VALUE_DROPDOWN_RESULT = "//*[@id='withOptGroup']/div/div[1]/div[1]"

    SELECT_ONE_DROPDOWN = "input[id='react-select-3-input']"
    SELECT_ONE_DROPDOWN_RESULT = "//*[@id='selectOne']/div/div[1]/div[1]"

    MULTISELECT_DROPDOWN = "input[id='react-select-4-input']"
    MULTISELECT_DROPDOWN_RESULTS = "div[class='css-12jo7m5']"
    REMOVE_ELEMENT_FROM_MULTISELECT = "div[class='css-1rhbuit-multiValue'] svg path"