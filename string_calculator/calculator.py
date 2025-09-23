import re

class StringCalculator:
    MAX_NUMBER = 1000
    DEFAULT_DELIMITER = ","
    NEWLINE = "\n"
    CUSTOM_DELIMITER_PREFIX = "//"
    MULTI_DELIMITER_PREFIX = "//["
    MULTI_DELIMITER_REGEX = r"\[(.*?)]"

    def __init__(self):
        pass

    @staticmethod
    def _handle_negatives(number_values):
        negatives = [x for x in number_values if x < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

    @classmethod
    def _extract_delimiters(cls, numbers):
        if numbers.startswith(cls.MULTI_DELIMITER_PREFIX):
            return re.findall(cls.MULTI_DELIMITER_REGEX, numbers)
        elif numbers.startswith(cls.CUSTOM_DELIMITER_PREFIX):
            return [numbers[2]]
        return [cls.DEFAULT_DELIMITER]

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = self._extract_delimiters(numbers)

        numbers_with_delimiter = numbers.replace(self.NEWLINE, self.DEFAULT_DELIMITER)
        pattern = "|".join(map(re.escape, delimiters))

        number_strings = re.split(pattern, numbers_with_delimiter)

        number_values = [
            int(value)
            for value in number_strings
            if value.lstrip('-').isdigit() and int(value) <= self.MAX_NUMBER
        ]
        self._handle_negatives(number_values)
        return sum(number_values)
