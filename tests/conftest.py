import pytest
import uuid
import pathlib


@pytest.fixture(scope="session")
def important_value():
    return "important_value"


@pytest.fixture(scope="session")
def file_name() -> str:
    """
    Return a file name that is unique for each test run.
    """
    file_name = f"test_file_{uuid.uuid4()}.txt"
    return file_name


@pytest.fixture(scope="session")
def setup_data_files(file_name: str) -> None:
    """
    Run a function, that writes some data to a file, and return the result
    of that function.

    At the end of the tessuite, run the teardown by executing the
    code after the yield statement.
    """

    yield return_data(file_name)

    # teardown

    file = pathlib.Path(file_name)
    file.unlink()


def return_data(file_name: str) -> str:
    """
    Write some data to a file and return the data written to the file.
    """
    test_data = "test data"

    with open(file_name, "w") as f:
        f.write(test_data)
    return test_data
