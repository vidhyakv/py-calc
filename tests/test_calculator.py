import pytest
from string_calculator.calculator import StringCalculator


@pytest.fixture
def sc():
    return StringCalculator()


def test_empty_string_returns_zero(sc):
    assert sc.add("") == 0