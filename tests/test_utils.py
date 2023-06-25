import pytest

from kur.utils import SortedList
from tests.conftests import correct_data


def test_data_json():
    data = SortedList().read_json()
    assert isinstance(data, list)
    assert isinstance(data[1], dict)


def test_true_list():
    data = SortedList()
    data.data = correct_data
    test_list = data.true_list()
    assert isinstance(test_list, list)
    assert isinstance(test_list[1], dict)
    assert len(test_list) == 100


def test_true_five_dict():
    data = SortedList().true_five_dict()
    assert isinstance(data, list)
    assert isinstance(data[1], dict)


def test_new_true_five_dict():
    data = SortedList().new_true_five_dict()
    assert isinstance(data, list)

