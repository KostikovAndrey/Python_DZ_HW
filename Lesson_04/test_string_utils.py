import pytest
from string_utils import StringUtils


class TestStringUtils:

    @pytest.mark.parametrize("input_str, expected", [
        ("skypro", "Skypro"),
        ("SKYPRO", "Skypro"),
        ("skypro academy", "Skypro academy"),
        ("123", "123"),
        ("тест", "Тест"),
        ("", ""),
        (" ", " "),
        ("a", "A"),
        ("тестовая строка 123", "Тестовая строка 123")
    ])
    def test_capitalize_positive(self, input_str, expected):
        utils = StringUtils()
        assert utils.capitalize(input_str) == expected

    @pytest.mark.parametrize("input_str", [None, 123, [], {}])
    def test_capitalize_negative_invalid_type(self, input_str):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.capitalize(input_str)

    @pytest.mark.parametrize("input_str, expected", [
        ("   skypro", "skypro"),
        ("skypro", "skypro"),
        ("   skypro   ", "skypro   "),
        ("", ""),
        ("   ", ""),
        ("   a   b   ", "a   b   "),
        ("текст с пробелами", "текст с пробелами")
    ])
    def test_trim_positive(self, input_str, expected):
        utils = StringUtils()
        assert utils.trim(input_str) == expected

    @pytest.mark.parametrize("input_str, delimiter, expected", [
        ("a,b,c,d", ",", ["a", "b", "c", "d"]),
        ("1:2:3:4", ":", ["1", "2", "3", "4"]),
        ("", ",", []),
        ("a", ",", ["a"]),
        ("a;b;c", ";", ["a", "b", "c"]),
        ("test", "", ["t", "e", "s", "t"])
    ])
    def test_to_list_positive(self, input_str, delimiter, expected):
        utils = StringUtils()
        assert utils.to_list(input_str, delimiter) == expected

    @pytest.mark.parametrize("input_str, delimiter", [
        (None, ","),
        (123, ",")
    ])
    def test_to_list_negative_invalid_type(self, input_str, delimiter):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.to_list(input_str, delimiter)

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "k", True),
        ("SkyPro", "z", False),
        ("", "a", False),
        ("test", "", False),
        ("123", "1", True),
        ("строка", "с", True)
    ])
    def test_contains_positive(self, string, symbol, expected):
        utils = StringUtils()
        assert utils.contains(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "S", "kyPro"),
        ("SkyPro", "y", "SkPro"),
        ("", "a", ""),
        ("test", "", "test"),
        ("aaaaa", "a", ""),
        ("test test", "t", "es es")
    ])
    def test_delete_symbol_positive(self, string, symbol, expected):
        utils = StringUtils()
        assert utils.delete_symbol(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "S", True),
        ("SkyPro", "k", False),
        ("", "S", False),
        ("test", "t", True),
        ("123", "1", True),
        (" ", " ", True)
    ])
    def test_starts_with_positive(self, string, symbol, expected):
        utils = StringUtils()
        assert utils.starts_with(string, symbol) == expected

    @pytest.mark.parametrize("string, symbol, expected", [
        ("SkyPro", "o", True),
        ("SkyPro", "O", False),
        ("", "o", False),
        ("test", "t", True),
        ("123", "3", True),
        (" ", " ", True)
    ])
    def test_end_with_positive(self, string, symbol, expected):
        utils = StringUtils()
        assert utils.end_with(string, symbol) == expected

    @pytest.mark.parametrize("input_str, expected", [
        ("", True),
        (" ", True),
        ("   ", True),
        ("test", False),
        ("   test   ", False),
        ("123", False),
        (None, True)
    ])
    def test_is_empty_positive(self, input_str, expected):
        utils = StringUtils()
        assert utils.is_empty(input_str) == expected

    @pytest.mark.parametrize("lst, joiner, expected", [
        ([1, 2, 3, 4], ", ", "1, 2, 3, 4"),
        (["a", "b", "c"], "-", "a-b-c"),
        ([], ", ", ""),
        ([1], ", ", "1"),
        (["test", 123, True], " | ", "test | 123 | True")
    ])
    def test_list_to_string_positive(self, lst, joiner, expected):
        utils = StringUtils()
        assert utils.list_to_string(lst, joiner) == expected

    @pytest.mark.parametrize("lst, joiner", [
        (None, ", "),
        (123, ", ")
    ])
    def test_list_to_string_negative_invalid_type(self, lst, joiner):
        utils = StringUtils()
        with pytest.raises(AttributeError):
            utils.list_to_string(lst, joiner)
