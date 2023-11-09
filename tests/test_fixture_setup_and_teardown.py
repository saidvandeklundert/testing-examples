"""
The (contrived) setup_data_files fixture is a fixture that is setup for the session scope.

It creates a file and returns some data using the yield statement.

At the end of the test session, the code after the yield statement is executed. Effectively,
this code is the tear down of the fixture.

In this example, the tear down of the fixture means removing the file.

To 'prove' this works, invoke the test suite and observe the fact that the file:
- is created
- is accessisble from other testing functions
- removed at the end of the test session, not immediately after the test function that
 uses the fixture

 
"""
import pathlib


def test_setup_data_files_validation(setup_data_files: str) -> None:
    """
    Test that the data returned from the setup_data_files fixture is
    correct.
    """
    assert setup_data_files == "test data"


def test_read_file_created_by_fixture(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = f.read()
    assert data == "test data"


def test_ensure_file_is_created(file_name: str) -> None:
    file = pathlib.Path(file_name)

    assert file.exists() is True
