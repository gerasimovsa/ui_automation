import pandas as pd
import datetime
import random

from dateutil.relativedelta import relativedelta


class Utils:

    @staticmethod
    def join_string(str_list: list[str]) -> str:
        return ",".join(str_list)

    @staticmethod
    def format_checkbox_strings(str_list: list[str]) -> list[str]:
        return [str.replace(' ', '').replace('doc', '').replace('.', '').lower() for str in str_list]

    @staticmethod
    def remove_newline(str_list: list[str]) -> list[str]:
        return [str.replace("\n", " ").lower() for str in str_list]

    @staticmethod
    def years_delta_from_now(start_date: str) -> str:
        date1 = datetime.datetime.strptime(start_date, '%d %b %Y')
        today = datetime.datetime.now()
        delta = str(relativedelta(today, date1).years)
        return delta

    @staticmethod
    def trim_string_end(string: str) -> str:
        chars_to_trim = len(string)-random.randint(1, 2)
        return string[0:chars_to_trim]

    @staticmethod
    def random_15_minutes_interval_time() -> str:
        time_list = pd.date_range("00:00", "23:59", freq="15min").strftime("%H:%M").to_list()
        return time_list[random.randint(0, len(time_list)-1)]