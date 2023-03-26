import random


class PracticeFormPageLocators:
    # forms
    FIRST_NAME = "input[id='firstName']"
    LAST_NAME = "input[id='lastName']"
    EMAIL = "input[id='userEmail']"
    RANDOM_GENDER_RADIO = f"label[for='gender-radio-{random.randint(1, 3)}']"
    PHONE_NUMBER = "input[id='userNumber']"
    DATE_OF_BIRTH = "input[id='dateOfBirthInput']"

    # datepicker
    DATEPICKER_YEAR = "select[class='react-datepicker__year-select']"
    DATEPICKER_MONTH = "select[class='react-datepicker__month-select']"
    DATEPICKER_DAY = ".//div[@class='react-datepicker__week']//div"

    SUBJECT = "input[id='subjectsInput']"
    RANDOM_HOBBY_CHECKBOX = f"label[for='hobbies-checkbox-{random.randint(1, 3)}']"
    UPLOAD_PICTURE = "input[id='uploadPicture']"
    CURRENT_ADDRESS = "textarea[id='currentAddress']"
    STATE_DROPDOWN = "div[id='state']"
    STATE_INPUT = "input[id='react-select-3-input']"
    CITY_DROPDOWN = "div[id='city']"
    CITY_INPUT = "input[id='react-select-4-input']"
    SUBMIT = "button[id='submit']"

    # created table
    STUDENT_NAME = "//tbody/tr[1]/td[2]"
    STUDENT_EMAIL = "//tbody/tr[2]/td[2]"
    STUDENT_GENDER = "//tbody/tr[3]/td[2]"
    STUDENT_PHONE = "//tbody/tr[4]/td[2]"
    STUDENT_DATE_OF_BIRTH = "//tbody/tr[5]/td[2]"
    STUDENT_SUBJECT = "//tbody/tr[6]/td[2]"
    STUDENT_HOBBIES = "//tbody/tr[7]/td[2]"
    STUDENT_PICTURE = "//tbody/tr[8]/td[2]"
    STUDENT_ADDRESS = "//tbody/tr[9]/td[2]"
    STUDENT_STATE_AND_CITY = "//tbody/tr[10]/td[2]"
    CLOSE_BUTTON = "button[id='closeLargeModal']"

    TABLE_DATA_LOCATORS = [STUDENT_NAME, STUDENT_EMAIL,
                           STUDENT_GENDER, STUDENT_PHONE,
                           STUDENT_DATE_OF_BIRTH, STUDENT_SUBJECT,
                           STUDENT_HOBBIES, STUDENT_PICTURE,
                           STUDENT_ADDRESS, STUDENT_STATE_AND_CITY]
