import urllib.request
from urllib.error import URLError
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


def test_conn():
    json_test1 = """{"currentDateTime":"2021-12-01"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test1)) :
        test1 = what_is_year_now()
    output1 = 2021
    assert test1 == output1

    json_test2 = """{"currentDateTime":"01.01.2021"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test2)) :
        test2 = what_is_year_now()
    output2 = 2021
    assert test2 == output2

    json_test3 = """{"currentDateTime":"11 12 13 14"}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test3)):
        with pytest.raises(ValueError):
            what_is_year_now()

    json_test4 = """{"currentDateTime":11}"""
    with patch.object(urllib.request, 'urlopen', return_value=io.StringIO(json_test4)):
        with pytest.raises(TypeError):
            what_is_year_now()


