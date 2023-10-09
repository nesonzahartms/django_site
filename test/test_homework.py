import pytest
import re


def numb(number):
    if not isinstance(number, int):
        raise TypeError("Введите целое число")
    return number % 2 == 0


@pytest.mark.parametrize('number, expected_result', [
    (2, True),
    (0, True),
    (-2, True),
    (1, False),
    (-1, False),
    (3, False),
    (4, True)
])
def test_numb(number, expected_result):
    assert numb(number) == expected_result


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


@pytest.mark.parametrize('string, expected_result', [
    ('Test123', True),
    ('test', True),
    ('123', True),
    ('Test123!', False),
    ('test-', False),
    ('', False)
])
def test_valid_string(string, expected_result):
    assert valid_string(string) == expected_result
