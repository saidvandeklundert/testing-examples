import pytest
import os


@pytest.mark.skip(reason="cannot make this work")
def test_this_fails():
    assert True is False


@pytest.mark.skipif(True, reason="skipped becuase this evaluates to 'True'")
def test_skip_using_skip_if():
    assert True is False


@pytest.mark.skipif(os.getenv("STAGE") != "INTEG", reason="only runs in integ stage")
def test_during_integ_stage():
    assert True is False
