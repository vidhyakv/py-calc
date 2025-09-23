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
        negatives = [x for x in self._numbers if x < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

    def _extract_delimiters(self):
        if self._numbers_str.startswith(self.MULTI_DELIMITER_PREFIX):
            return re.findall(self.MULTI_DELIMITER_REGEX, self._numbers_str)
        elif self._numbers_str.startswith(self.CUSTOM_DELIMITER_PREFIX):
            return [self._numbers_str[len(self.CUSTOM_DELIMITER_PREFIX)]]
        return [self.DEFAULT_DELIMITER]

    def _remove_custom_delimiter(self):
        if self._numbers_str.startswith(self.CUSTOM_DELIMITER_PREFIX):
            self._numbers_str = self._numbers_str.split(self.NEWLINE, 1)[1]

    def _normalize_newlines(self):
        self._numbers_str = self._numbers_str.replace(self.NEWLINE, self.DEFAULT_DELIMITER)

    def _split_numbers(self, delimiters):
        pattern = "|".join(map(re.escape, delimiters))
        number_strings = re.split(pattern, self._numbers_str)
        self._numbers = [
            int(value)
            for value in number_strings
            if value.lstrip('-').isdigit() and int(value) <= self.MAX_NUMBER
        ]

    def add(self, numbers_str: str) -> int:
        if not numbers_str:
            return 0

        self._numbers_str = numbers_str
        delimiters = self._extract_delimiters()
        self._remove_custom_delimiter()
        self._normalize_newlines()
        self._split_numbers(delimiters)
        self._handle_negatives()
        return sum(self._numbers)
