import math


class Fraction:
    def __init__(self, numerator: int = 1, denominator: int = 1):
        self.numerator = numerator
        self.denominator = denominator
        self._reduce()

    def plus(self, fraction: "Fraction"):
        nominator = self.numerator * fraction.denominator + fraction.numerator * self.denominator
        denominator = self.denominator * fraction.denominator
        return Fraction(nominator, denominator)

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (
                self.numerator == other.numerator
                and self.denominator == other.denominator
            )
        return False

    def __str__(self):
        return f"{self.numerator} / {self.denominator}"

    def _reduce(self):
        g = math.gcd(self.numerator, self.denominator)
        if self.denominator < 0:
            g = -g
        self.numerator //= g
        self.denominator //= g
