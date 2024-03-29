from src.functions import multiply
import pytest


# paramatrize:
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 2, 4),
        (2, 10, 20),
        (10, 10, 100),
    ],
)
def test_multiply_simple_paramatrization(x, y, expected):
    result = multiply(x, y)
    assert result == expected


# paramatrize using test data:
TEST_DATA = [
    (2, 2, 4),
    (6, 6, 36),
    (1, 1, 1),
    (1, 8, 8),
]


@pytest.mark.parametrize(
    "x, y, expected",
    TEST_DATA,
)
def test_multiply_using_paramatrization_data(x, y, expected):
    assert multiply(x, y) == expected


# paramatrize using several lists:
X_VALUES = [2, 6, 1, 1]
Y_VALUES = [2, 6, 1, 8]
EXPECTED = [4, 36, 1, 8]


@pytest.mark.parametrize(
    "x, y, expected",
    list(zip(X_VALUES, Y_VALUES, EXPECTED)),
)
def test_multiply_using_paramatrization_data_using_zip(x, y, expected):
    assert multiply(x, y) == expected


# stacking paramatrization decorator:
@pytest.mark.parametrize(
    "y",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
        (7),
        (8),
        (9),
    ],
)
@pytest.mark.parametrize(
    "x",
    [
        (1),
        (2),
        (3),
        (4),
        (5),
        (6),
        (7),
        (8),
        (9),
    ],
)
def test_multiply_stacked_paramatrization(x, y):
    """
    Not testing for output, testing that the func can run
    without throwing errors.
    """
    assert isinstance(multiply(x, y), int)


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 2, 4),
    ],
)
def test_multiply_simple_paramatrization_and_fixture_1(x, y, expected, important_value):
    assert important_value == "important_value"
    result = multiply(x, y)
    assert result == expected


@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 2, 4),
    ],
)
def test_multiply_simple_paramatrization_and_fixture_2(important_value, x, y, expected):
    assert important_value == "important_value"
    result = multiply(x, y)
    assert result == expected
