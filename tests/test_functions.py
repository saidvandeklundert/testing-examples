from src.functions import multiply


def test_multiply():
    """
    A unit test that tests that multiply function.
    """
    result = multiply(2, 4)
    assert result == 8
