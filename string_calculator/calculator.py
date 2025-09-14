class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        newLineSymbol = "\n"
        defaultDelimiter = ","
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split(newLineSymbol, 1)
            defaultDelimiter = delimiter_line[2:]

        numbers_with_commas = numbers.replace(newLineSymbol, defaultDelimiter)
        split_numbers = numbers_with_commas.split(defaultDelimiter)
        converted_integers = [int(num) for num in split_numbers]

        return sum(converted_integers)
