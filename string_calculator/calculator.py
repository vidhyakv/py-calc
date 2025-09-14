class StringCalculator:
    def __init__(self):
        pass

    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        defaultDelimiter = ","
        newLineDelimiter = "\n"

        numbers = numbers.replace(newLineDelimiter, defaultDelimiter)
        parts = numbers.split(",")
        return sum(int(p) for p in parts)
