import re


def handle_negatives(number_values):
    negatives = [x for x in number_values if x < 0]
    if negatives:
        raise ValueError(f"Negatives not allowed: {negatives}")


def extract_delimiters(numbers):
    MAX_NUMBER = 1000
    DEFAULT_DELIMITER = ","
    NEWLINE = "\n"
    CUSTOM_DELIMITER_PREFIX = "//"
    MULTI_DELIMITER_PREFIX = "//["
    MULTI_DELIMITER_REGEX = r"\[(.*?)]"
    DEFAULT_DELIMITER = ","


    delimiters = [DEFAULT_DELIMITER]

    if numbers.startswith(CUSTOM_DELIMITER_PREFIX):
        delimiter_definition, numbers = numbers.split(NEWLINE, 1)
        custom_delimiters = delimiter_definition[len(CUSTOM_DELIMITER_PREFIX):]

        if delimiter_definition.startswith(MULTI_DELIMITER_PREFIX):
            delimiters = re.findall(MULTI_DELIMITER_REGEX, custom_delimiters)
        else:
            delimiters = [custom_delimiters]


    return delimiters , numbers


class StringCalculator:
    MAX_NUMBER = 1000
    DEFAULT_DELIMITER = ","
    NEWLINE = "\n"
    CUSTOM_DELIMITER_PREFIX = "//"
    MULTI_DELIMITER_PREFIX = "//["
    MULTI_DELIMITER_REGEX = r"\[(.*?)]"

    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters , numbers = extract_delimiters(numbers)

        numbers_with_delimiter = numbers.replace(self.NEWLINE, self.DEFAULT_DELIMITER)
        pattern = "|".join(map(re.escape, delimiters))

        number_strings = re.split(pattern, numbers_with_delimiter)

        number_values = [
            int(value)
            for value in number_strings
            if value.lstrip('-').isdigit() and int(value) <= self.MAX_NUMBER
        ]
        handle_negatives(number_values)
        return sum(number_values)
