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


def test_custom_delimiter(sc):
    assert sc.add("//;\n1;2") == 3
    assert sc.add("//|\n4|5|6") == 15


def test_negative_numbers_raise_exception(sc):
    with pytest.raises(ValueError) as exc:
        sc.add("1,-2,3")
    assert "Negatives not allowed" in str(exc.value)


def test_numbers_bigger_than_1000_are_ignored(sc):
    assert sc.add("2,1001") == 2
    assert sc.add("1000,2") == 1002


def test_delimiter_of_any_length(sc):
    assert sc.add("//[***]\n1***2***3") == 6
    assert sc.add("//[abc]\n4abc5abc6") == 15


def test_multiple_delimiters(sc):
    assert sc.add("//[*][%]\n1*2%3") == 6


def test_multiple_long_delimiters(sc):
    assert sc.add("//[***][%%%]\n1***2***3") == 6
    assert sc.add("//[***][%%%]\n1***2%%%3***4%%%5") == 15
    assert sc.add("//[***][$$][%%%]\n1***2%%%3***4%%%5$$6") == 21
    assert sc.add("//[***][$$][%%%]\n1***2%%%3***4%%%5$$$6") == 15

@pytest.mark.parametrize("a,b, expected",[(1,2,3),(3,4,7)])
def test_with_parameter(a,b, expected, sc):
    assert sc.add(f"{a},{b}") == expected