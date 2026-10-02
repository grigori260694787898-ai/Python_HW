import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("skypro", "skypro"),
    ("", ""),
])
def test_trim(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "s"),
    ("world", "w"),
    ("python", "n"),
])

def test_symbol_positive(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is True

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("skypro", "q"),
    ("world", "y"),
    ("python", "r"),
])

def test_symbol_negative(input_str, symbol):
    assert string_utils.contains(input_str, symbol) is False

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", "kypro"),
    ("python", "n", "pytho"),
    ("hello world", " ", "helloworld"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "q", "skypro"),
    ("", "a", ""),
    ("   ", " ", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
