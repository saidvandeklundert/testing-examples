import os

GLOBAL_DICT = {"a": 1, "b": 2, "c": 3}


def operations() -> str:
    if os.getenv("STAGE") == "PROD":
        return "Doing the things prod"
    elif os.getenv("STAGE") == "BETA":
        return "Doing the things beta"
    return "default"


def get_dict() -> dict:
    return GLOBAL_DICT
