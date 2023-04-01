import os
from unittest import mock
from unittest.mock import MagicMock
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


@mock.patch.dict("src.dict_and_env.GLOBAL_DICT", {"a": "PATCHED DICT"})
def test_get_dict_mock_single_key():
    """
    Patch a key in the GLOBAL_DICT var from the 'dict_and_env' module.
    """
    resulting_dict = dict_and_env.get_dict()
    assert resulting_dict == {"a": "PATCHED DICT", "b": 2, "c": 3}


@mock.patch.dict("src.dict_and_env.GLOBAL_DICT", {"c": "PATCHED"})
@mock.patch.dict("src.dict_and_env.GLOBAL_DICT", {"b": "THE"})
@mock.patch.dict("src.dict_and_env.GLOBAL_DICT", {"a": "ENTIRE DICT"})
def test_get_dict_mock_multiple_keys():
    """
    Patching multiple keys in the GLOBAL_DICT var from the 'dict_and_env' module.
    """
    resulting_dict = dict_and_env.get_dict()
    assert resulting_dict == {
        "c": "PATCHED",
        "b": "THE",
        "a": "ENTIRE DICT",
    }
