class Fraction:
    def __init__(self, numerator: int = 1, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator

    def plus(self, fraction: "Fraction"):
        return Fraction(self.numerator + fraction.numerator, self.denominator)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )
        return False
