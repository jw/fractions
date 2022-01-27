import pytest

from fractions.fractions import Fraction


def test_zero_plus_zero():
    assert Fraction(0).plus(Fraction(0)) == Fraction(0)
    assert Fraction(0, 1).plus(Fraction(0, 1)) == Fraction(0)
    assert Fraction(0, 1).plus(Fraction(0, -1)) == Fraction(0)


def test_plus_same_denominator():
    assert Fraction(1, 2).plus(Fraction(2, 2)) == Fraction(3, 2)
    assert Fraction(2, 4).plus(Fraction(-2, 4)) == Fraction(0)
    assert Fraction(-1, 2).plus(Fraction(-2, 2)) == Fraction(-3, 2)


def test_plus_different_denominator():
    assert Fraction(1, 2).plus(Fraction(2, 3)) == Fraction(7, 6)
    assert Fraction(1, 2).plus(Fraction(-2, 3)) == Fraction(-1, 6)
    assert Fraction(4, 8).plus(Fraction(5, 15)) == Fraction(5, 6)


def test_reduce():
    assert Fraction(42) == Fraction(42)
    assert Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(6, 8) == Fraction(3, 4)
    assert Fraction(6) == Fraction(24, 4)


def test_equality():
    assert Fraction(1) == Fraction(1, 3).plus(Fraction(2, 3))
    assert Fraction(1, 2) == Fraction(-1, -2)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        Fraction(1, 0)
