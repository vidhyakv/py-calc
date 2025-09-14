class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        numbers_with_commas = numbers.replace("\n", ",")
        split_numbers = numbers_with_commas.split(",")
        converted_integers = [int(num) for num in split_numbers]

        return sum(converted_integers)
