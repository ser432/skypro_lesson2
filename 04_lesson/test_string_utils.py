import pytest
from string_utils import StringUtils

utils = StringUtils()


# --- 1. Тесты для метода capitalize ---

def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"


def test_capitalize_digits():
    assert utils.capitalize("123") == "123"


def test_capitalize_negative_empty():
    assert utils.capitalize("") == ""


def test_capitalize_negative_spaces():
    assert utils.capitalize(" ") == " "


def test_capitalize_negative_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)


# --- 2. Тесты для метода trim ---

def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"


def test_trim_with_spaces_in_phrase():
    assert utils.trim("   04 апреля 2023") == "04 апреля 2023"


def test_trim_negative_empty():
    assert utils.trim("") == ""


def test_trim_negative_spaces():
    assert utils.trim("   ") == ""


def test_trim_negative_none():
    with pytest.raises(AttributeError):
        utils.trim(None)


# --- 3. Тесты для метода contains ---

def test_contains_true():
    assert utils.contains("SkyPro", "S") is True


def test_contains_false():
    assert utils.contains("SkyPro", "U") is False


def test_contains_negative_empty_string():
    assert utils.contains("", "a") is False


def test_contains_negative_empty_symbol():
    assert utils.contains("SkyPro", "") is True


def test_contains_negative_none():
    with pytest.raises(AttributeError):
        utils.contains(None, "a")


# --- 4. Тесты для метода delete_symbol ---

def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"


def test_delete_symbol_part():
    assert utils.delete_symbol("SkyPro", "Pro") == "Sky"


def test_delete_symbol_not_found():
    assert utils.delete_symbol("SkyPro", "U") == "SkyPro"


def test_delete_symbol_negative_empty():
    assert utils.delete_symbol("", "a") == ""


def test_delete_symbol_negative_none():
    with pytest.raises(AttributeError):
        utils.delete_symbol(None, "a")
