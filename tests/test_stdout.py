from src.generate_some_stdout import message_to_stdout
import pytest


def test_stdout_pass(capsys):
    """
    Test that the message_to_stdout() function prints the expected string.
    """
    message_to_stdout()
    captured = capsys.readouterr()
    assert captured.out == "testing is tedious and more fun with good examples\n"


@pytest.mark.xfail
def test_stdout_fail(capsys):
    """
    We use mark.xfail because we expect this test to fail.
    """
    message_to_stdout()
    captured = capsys.readouterr()
    assert captured.out == "THIS IS NOT THE EXPECTED OUTPUT\n"
