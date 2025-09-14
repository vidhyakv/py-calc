class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]

        numbers_with_commas = numbers.replace("\n", delimiter)
        split_numbers = numbers_with_commas.split(delimiter)
        converted_integers = [int(num) for num in split_numbers]

        return sum(converted_integers)
