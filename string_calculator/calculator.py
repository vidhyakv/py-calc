class StringCalculator:
    MAX_NUMBER = 1000
    DEFAULT_DELIMITER = ","
    NEWLINE = "\n"
    CUSTOM_DELIMITER_PREFIX = "//"

    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = self.DEFAULT_DELIMITER

        if numbers.startswith(self.CUSTOM_DELIMITER_PREFIX):
            delimiter_definition, numbers = numbers.split(self.NEWLINE, 1)
            delimiter = delimiter_definition[len(self.CUSTOM_DELIMITER_PREFIX):]

        numbers_with_delimiter = numbers.replace(self.NEWLINE, delimiter)
        number_strings = numbers_with_delimiter.split(delimiter)

        number_values = [num for value in number_strings if (num := int(value)) <= self.MAX_NUMBER]

        negatives = [x for x in number_values if x < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(number_values)
