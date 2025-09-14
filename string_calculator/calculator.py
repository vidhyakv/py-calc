class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        newline = "\n"
        default_delimiter = ","

        if numbers.startswith("//"):
            delimiter_definition, numbers = numbers.split(newline, 1)
            default_delimiter = delimiter_definition[2:]

        numbers_with_default_delimiter = numbers.replace(newline, default_delimiter)
        number_strings = numbers_with_default_delimiter.split(default_delimiter)
        number_values = [int(value) for value in number_strings]

        negatives = [x for x in number_values if x < 0]
        if negatives:
            raise ValueError(f"Negatives not allowed: {negatives}")

        return sum(number_values)
