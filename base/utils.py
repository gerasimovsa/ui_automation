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


