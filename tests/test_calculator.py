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

def test_multiple_numbers_returns_sum(sc):
    assert sc.add("1,2,3") == 6
    assert sc.add("5,5,5,5") == 20

def test_newline_as_delimiter(sc):
    assert sc.add("1\n2,3") == 6
    assert sc.add("10\n20\n30") == 60



