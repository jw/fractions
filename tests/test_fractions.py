from factions.fractions import Fraction


def test_zero_plus_zero():
    assert Fraction(0).plus(Fraction(0)) == Fraction(0)
