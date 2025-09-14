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

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [self.DEFAULT_DELIMITER]

        if numbers.startswith(self.CUSTOM_DELIMITER_PREFIX):
            delimiter_definition, numbers = numbers.split(self.NEWLINE, 1)
            custom_part = delimiter_definition[len(self.CUSTOM_DELIMITER_PREFIX):]

            if delimiter_definition.startswith(self.MULTI_DELIMITER_PREFIX):
                delimiters = re.findall(self.MULTI_DELIMITER_REGEX, custom_part)
            else:
                delimiters = [custom_part]

        numbers_with_delimiter = numbers.replace(self.NEWLINE, self.DEFAULT_DELIMITER)
        pattern = "|".join(map(re.escape, delimiters))

        number_strings = re.split(pattern,numbers_with_delimiter)

        number_values = [
            int(value)
            for value in number_strings
            if value.lstrip('-').isdigit() and int(value) <= self.MAX_NUMBER
        ]

        negatives = [x for x in number_values if x < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(number_values)
