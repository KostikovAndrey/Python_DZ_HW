class StringUtils:

    def capitalize(self, string: str) -> str:

        if not string:
            return string
        if len(string) > 1:
            return string[0].upper() + string[1:].lower()
        return string[0].upper()

    def trim(self, string: str) -> str:

        if not string:
            return string
        start = 0
        while start < len(string) and string[start] == ' ':
            start += 1
        return string[start:]

    def to_list(self, string: str, delimiter: str = ",") -> list:

        if not string:
            return []
        return string.split(delimiter)

    def contains(self, string: str, symbol: str) -> bool:

        if not string or not symbol:
            return False
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:

        if not string or not symbol:
            return string
        return string.replace(symbol, "")

    def starts_with(self, string: str, symbol: str) -> bool:

        if not string or not symbol:
            return False
        return string[0] == symbol

    def end_with(self, string: str, symbol: str) -> bool:

        if not string or not symbol:
            return False
        return string[-1] == symbol

    def is_empty(self, string: str) -> bool:

        return string is None or string == "" or string.strip() == ""

    def list_to_string(self, lst: list, joiner: str = ", ") -> str:

        if not lst:
            return ""
        return joiner.join(str(item) for item in lst)
