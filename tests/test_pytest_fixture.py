"""
Corner case where you might want to test the test functions and you run
into a situation where you need to put functions that 'are' fixtures under test.

A problem associated with this is fixture functions cannot be called directly: you need to 
'neutralize' the fixture decorator.

After having tested the function decorated with 'pytest.fixture', you will still want to be able
to use the regular fixtures associated with the current pytest run.

This example does just that. It patches the fixture with a decorator that wraps a function without
 'doing' anything.

After haing put the function that is a fixture under test, we run another test function
 that is using a fixture defined in the conftest.py. We show that this is still working.
"""
from unittest.mock import patch
from functools import wraps
import pytest

pytestmark = pytest.mark.data


def mock_decorator(*args, **kwargs):
    """Does nothing, allows everything."""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            return f(*args, **kwargs)

        return decorated_function

    return decorator


# patch the fixture decorater prior to importing the decorated functions:
patch("pytest.fixture", mock_decorator).start()

from src.testing_pipeline import data


def test_data():
    seed = [1, 2, 3]

    result = data(seed)
    assert result == [2, 3, 4]


patch("pytest.fixture", mock_decorator).stop


def test_fixtures_still_work(important_value, request):
    """
    The 'normal' fixtures that are used in the pipeline still work
    despite the fixture decorator being patched
    """
    # import pdb

    # pdb.set_trace()
    # request.config.invocation_params.args
    assert important_value == "important_value"
