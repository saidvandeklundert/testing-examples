import os
from unittest import mock
from src import dict_and_env


@mock.patch.dict(os.environ, {"STAGE": "PROD"})
def test_prod_return():
    resulting_operation = dict_and_env.operations()
    assert resulting_operation == "Doing the things prod"


@mock.patch.dict(os.environ, {"STAGE": "BETA"})
def test_beta_return():
    resulting_operation = dict_and_env.operations()
    assert resulting_operation == "Doing the things beta"


@mock.patch.dict(os.environ, {"STAGE": "SOMETHING_ELSE"})
def test_default_return():
    resulting_operation = dict_and_env.operations()
    assert resulting_operation == "default"
