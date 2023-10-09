import pytest
import json
from utils import func


def test_load_data_file():
    assert func.load_data_file('test.json') == [{'1': '25'}, {'2': '36'}]
    assert func.load_data_file('test2.json') == [{}]
    assert func.load_data_file('test5.json') is None
    with pytest.raises(json.decoder.JSONDecodeError):
        func.load_data_file('test3.json')


def test_date_format():
    assert func.date_format("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert func.date_format("2022-05-01 18:35:29.512364") == "01.05.2022"
    with pytest.raises(TypeError):
        func.date_format(512364)
    with pytest.raises(ValueError):
        func.date_format("2019-07-03U18:35:29.512364")


def test_masks_numbers():
    assert func.masks_numbers("MasterCard 7158300734726758") == "MasterCard 7158 30** **** 6758"
    assert func.masks_numbers("Visa GolD S P C 2435782645913354") == "Visa GolD S P C 2435 78** **** 3354"
    assert func.masks_numbers("Calculation 12345678984513697125") == "Calculation **7125"
    assert func.masks_numbers("Calc 125") == "Calc **125"
    with pytest.raises(AttributeError):
        func.masks_numbers(12345678984513697125)


def test_filters_sorts():
    assert func.filters_sorts([{"A": "1", "B": "6"},
                               {"A": "0", "B": "8"},
                               {"A": "1", "B": "3"}],
                              ("A", "1"), "B") == [{"A": "1", "B": "6"}, {"A": "1", "B": "3"}]
    assert func.filters_sorts([{"A": "1", "B": "6"},
                               {"A": "0", "B": "8"},
                               {"A": "1", "B": "3"}],
                              ("A", "1"), "B", rev=False, line_counter=1) == [{"A": "1", "B": "3"}]

