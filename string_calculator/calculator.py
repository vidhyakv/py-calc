class StringCalculator:
    def add(self, numbers: str) -> int:
        if numbers == "":
            return 0
        parts = numbers.split(",")
        if len(parts) == 1:
            return int(parts[0])
        return int(parts[0]) + int(parts[1])
