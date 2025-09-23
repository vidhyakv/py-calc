import re

class StringCalculator:
    MAX_NUMBER = 1000
    DEFAULT_DELIMITER = ","
    NEWLINE = "\n"
    CUSTOM_DELIMITER_PREFIX = "//"
    MULTI_DELIMITER_PREFIX = "//["
    MULTI_DELIMITER_REGEX = r"\[(.*?)]"

    def __init__(self):
        self._numbers_str = ""
        self._numbers = []

    def _handle_negatives(self):
        negatives = [x for x in self._numbers if x < 0]  # check parsed numbers, not string
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

    def _extract_delimiters(self):
        if self._numbers_str.startswith(self.MULTI_DELIMITER_PREFIX):
            return re.findall(self.MULTI_DELIMITER_REGEX, self._numbers_str)
        elif self._numbers_str.startswith(self.CUSTOM_DELIMITER_PREFIX):
            return [self._numbers_str[2]]
        return [self.DEFAULT_DELIMITER]

    def _remove_custom_delimiter(self):
        if self._numbers_str.startswith(self.CUSTOM_DELIMITER_PREFIX):
            self._numbers_str = self._numbers_str.split(self.NEWLINE, 1)[1]

    def add(self, numbers_str: str) -> int:
        if not numbers_str:
            return 0

        self._numbers_str = numbers_str
        delimiters = self._extract_delimiters()
        self._remove_custom_delimiter()

        numbers_with_delimiter = self._numbers_str.replace(self.NEWLINE, self.DEFAULT_DELIMITER)
        pattern = "|".join(map(re.escape, delimiters))

        self._numbers = [
            int(value)
            for value in re.split(pattern, numbers_with_delimiter)
            if value.lstrip('-').isdigit() and int(value) <= self.MAX_NUMBER
        ]

        self._handle_negatives()
        return sum(self._numbers)
