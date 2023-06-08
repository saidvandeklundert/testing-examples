import requests  # type: ignore


def tell_if_it_is_sunny(location: str) -> str:
    """
    Reaches out to an API and returns a string telling you whether or not
    it is currently sunny in the given location.

    This function is used in the examples to show how you can mock methods.

    The actual API does not exist, so this function cannot run as is.
    """
    url = f"https://nonexistingweatherservice/data/weather/{location}"
    api_response_str = requests.get(url)
    api_response_d = api_response_str.json()

    if "sunny" in api_response_d["currentConditions"]["comment"].lower():
        return f"It is sunny in {location}"
    else:
        return f"It is not sunny in {location}"
