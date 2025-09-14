class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        if numbers.isdigit():
            return int(numbers)
        return -1
