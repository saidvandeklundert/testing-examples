from src.generate_database_report import get_report
import pytest
from unittest import mock


@pytest.mark.skip(
    "This test is skipped because it takes too long and it is not deterministic."
)
def test_get_report():
    """
    This test has some problems.

    For one, it takes 5 seconds to run due to the other function it calls
    The second problem is that it is not deterministic. It gets random
    numbers from another function it calls. That makes it difficult to
    make proper assertions.
    """
    assert get_report() == 50000000000


@mock.patch("src.generate_database_report.get_database_data")
def test_get_report_mocked(mocked_get_database_data):
    """
    Mock the 'get_database_data' function to return a predictable value.

    The function is mocked to return a list of 2 numbers: 10 and 10.

    This makes it easy to test the rest of the logic in the 'get_report' function
    because all it really does is divive the sum of the numbers in the list by the
    length of the list. In this case;

    (10 + 10) / 2 = 10.
    """

    mocked_get_database_data.return_value = [
        10,
        10,
    ]
    assert get_report() == 10
