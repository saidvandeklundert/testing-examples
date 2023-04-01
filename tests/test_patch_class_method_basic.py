"""
python -m pytest .\tests\test_patch_class_method_basic.py
"""
from src.sunny import tell_if_it_is_sunny
from unittest import mock
import src


@mock.patch.object(src.sunny.requests, "get")
def test_tell_if_it_is_sunny(mocked_get):
    """
    Test that the 'tell_if_it_is_sunny' function returns the expected value.

    Patch the function where it is called, hence the 'src.sunny.requests' part.
    """
    mocked_get.return_value.json.return_value = {
        "currentConditions": {
            "comment": "It is sunny in New York",
        }
    }
    assert tell_if_it_is_sunny("New York") == "It is sunny in New York"
