import pytest
import simple_calculator as calc

def test_add_two_numbers():
    res = calc.add(1, 3)
    assert res == 4

def test_add_two_numbers_invalid():
    with pytest.raises(Exception) as e_info:
        res = calc.add("2", 3)
    assert str(e_info.value) == "Input should integer"

def test_add_numbers():
    res = calc.add(1, 3, 4, 5)
    assert res == 13


def test_substract_two_numbers():
    res = calc.sub(4, 2)
    assert res == 2


def test_substract_two_numbers_invalid():
    with pytest.raises(Exception) as e_info:
        res = calc.sub("4", 2)
    assert str(e_info.value) == "Input should integer"


def test_substract_numbers():
    res = calc.sub(6, 3, 4, 2)
    assert res == -3
