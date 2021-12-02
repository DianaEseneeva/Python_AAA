import urllib.request
import json
import pytest
from unittest.mock import patch
import io

API_URL = 'http://worldclockapi.com/api/json/utc/now'

YMD_SEP = '-'
YMD_SEP_INDEX = 4
YMD_YEAR_SLICE = slice(None, YMD_SEP_INDEX)

DMY_SEP = '.'
DMY_SEP_INDEX = 5
DMY_YEAR_SLICE = slice(DMY_SEP_INDEX + 1, DMY_SEP_INDEX + 5)


def what_is_year_now() -> int:
    """
    Получает текущее время из API-worldclock и извлекает из поля 'currentDateTime' год
    Предположим, что currentDateTime может быть в двух форматах:
      * YYYY-MM-DD - 2019-03-01
      * DD.MM.YYYY - 01.03.2019
    """
    with urllib.request.urlopen(API_URL) as resp:
        resp_json = json.load(resp)

    datetime_str = resp_json['currentDateTime']

    if datetime_str[YMD_SEP_INDEX] == YMD_SEP:
        year_str = datetime_str[YMD_YEAR_SLICE]
    elif datetime_str[DMY_SEP_INDEX] == DMY_SEP:
        year_str = datetime_str[DMY_YEAR_SLICE]
    else:
        raise ValueError('Invalid format')

    return int(year_str) 


def test_separator_1():
    json_test = """{"currentDateTime":"2021-12-01"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        test = what_is_year_now()
    output = 2021
    assert test == output


def test_separator_2():
    json_test = """{"currentDateTime":"01.01.2021"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        test = what_is_year_now()
    output = 2021
    assert test == output


def test_no_needed_separator():
    json_test = """{"currentDateTime":"11 12 13 14"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_wrong_type_of_input():
    json_test = """{"currentDateTime":11}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        with pytest.raises(TypeError):
            what_is_year_now()


def test_incorrect_json():
    json_test = """{}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        with pytest.raises(KeyError):
            what_is_year_now()


def test_correct_separator_1_exception():
    json_test = """{currentDateTime":"abcd-}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        with pytest.raises(ValueError):
            what_is_year_now()


def test_correct_separator_2_exception():
    json_test = """{currentDateTime":"dd.mm.year}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test)):
        with pytest.raises(ValueError):
            what_is_year_now()

