import pytest


@pytest.fixture(scope="session")
def data(seed_data: list[int]) -> list[int]:
    seed_data_list = [x + 1 for x in seed_data]
    return seed_data_list
