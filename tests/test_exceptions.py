import pytest
from under_test.functions import divide_small_numbers


def test_divide_small_numbers_exception():
    """
    Verify an Exception is raised when the input
    for 'divie_small_numbers' is too small.
    """
    with pytest.raises(Exception):
        divide_small_numbers(101, 1)


def test_divide_small_numbers_exceptions():
    """ """
    with pytest.raises(ValueError):
        divide_small_numbers(101, 1)

    with pytest.raises(ZeroDivisionError):
        divide_small_numbers(0, 0)


def test_divide_small_numbers_exception_content():
    """ """
    with pytest.raises(ValueError) as err:
        divide_small_numbers(101, 1)

    assert "Not accepting numbers over 100" in err.value.__str__()
