import pytest
from string_calculator.calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


def test_empty_string_returns_zero(sc):
    assert sc.add("") == 0

def test_non_empty_string_do_not_return_zero(sc):
    assert sc.add("1") != 0
