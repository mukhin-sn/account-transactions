import pytest
import json
from utils import func


def test_load_data_file():
    assert func.load_data_file('test.json') == [{'1': '25'}, {'2': '36'}]
    assert func.load_data_file('test2.json') == [{}]
    assert func.load_data_file('test5.json') is None
    with pytest.raises(json.decoder.JSONDecodeError):
        func.load_data_file('test3.json')
