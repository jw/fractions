from fractions.fractions import Fraction


def test_zero_plus_zero():
    assert Fraction(0).plus(Fraction(0)) == Fraction(0)
    assert Fraction(0, 1).plus(Fraction(0, 1)) == Fraction(0)


def test_positive_plus_same_denominator():
    assert Fraction(1, 2).plus(Fraction(2, 2)) == Fraction(3, 2)


def test_positive_plus_different_denominator():
    assert Fraction(1, 2).plus(Fraction(2, 3)) == Fraction(7, 6)


def test_reduce():
    assert Fraction(42) == Fraction(42)
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(6, 8) == Fraction(3, 4)
