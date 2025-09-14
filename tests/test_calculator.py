import pytest
from string_calculator.calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


def test_empty_string_returns_zero(sc):
    assert sc.add("") == 0

def test_non_empty_string_do_not_return_zero(sc):
    assert sc.add("1") != 0

def test_single_number_returns_value(sc):
    assert sc.add("1") == 1

def test_two_numbers_returns_sum(sc):
    assert sc.add("1,2") == 3
    assert sc.add("22,43") == 65

def test_multiple_numbers_returns_sum():
    calc = StringCalculator()
    assert calc.add("1,2,3") == 6
    assert calc.add("5,5,5,5") == 20


