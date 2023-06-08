import pytest


@pytest.fixture(scope="session")
def important_value():
    return "important_value"
