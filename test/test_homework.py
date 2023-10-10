import pytest
import re


def numb(number):
    if not isinstance(number, int):
        raise TypeError('NaN')
    return number % 2 == 0


@pytest.mark.parametrize('number, expected', [
    (2, True),
    (0, True),
    (4, True),
    (1, False),
    (5, False),
    (3, False),
    (10, True)
])
def test_numb(number, expected):
    assert numb(number) == expected


@pytest.mark.parametrize('number', [
    '2',
    2.5,
    [2],
    {'number': 2}
])
def test_numb_type_error(number):
    with pytest.raises(TypeError):
        numb(number)


def valid_string(string):
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, string))


@pytest.mark.parametrize('string, expected', [
    ('Test123', True),
    ('test', True),
    ('123', True),
    ('Test123!', False),
    ('test-', False),
    ('', False)
])
def test_valid_string(string, expected):
    assert valid_string(string) == expected
