from under_test.functions import multiply


def test_multiply():
    result = multiply(2, 4)
    assert result == 8
