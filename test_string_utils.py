import pytest
from string_utils import StringUtils


string_utils = StringUtils()



@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected



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
@pytest.mark.parametrize("self, utils", [
])

def test_delete_symbol_positive(self, utils):
    assert utils.delete_simbol(skypro, s) == "kypro"



@pytest.mark.negaative
@pytest.mark.parametrize("self, utils", [
])

def test_delete_symbol_positive1(self, utils):
    assert utils.delete_simbol(python, n) == "python"
