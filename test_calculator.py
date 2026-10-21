"""Изолированные параметризованные проверки всех методов Calculator."""

import pytest

from calculator import Calculator


@pytest.mark.parametrize(
    "first,second,expected",
    [
        (2, 3, 5),
        (-4, -6, -10),
        (-4, 7, 3),
        (0, 9, 9),
    ],
)
def test_add(first, second, expected):
    assert Calculator().add(first, second) == expected


@pytest.mark.parametrize(
    "dividend,divisor,expected",
    [
        (8, 2, 4.0),
        (-9, 3, -3.0),
        (9, -3, -3.0),
        (5, 2, 2.5),
        (0, 5, 0.0),
    ],
)
def test_divide(dividend, divisor, expected):
    assert Calculator().divide(dividend, divisor) == expected


@pytest.mark.parametrize("dividend", [5, 0])
def test_divide_by_zero(dividend):
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(dividend, 0)


@pytest.mark.parametrize(
    "number,expected",
    [
        (-7, False),
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (9, False),
        (17, True),
        (25, False),
        (29, True),
    ],
)
def test_is_prime_number(number, expected):
    assert Calculator().is_prime_number(number) is expected
