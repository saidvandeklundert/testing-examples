import time
import random
from typing import List


def get_database_data() -> List[int]:
    time.sleep(5)
    return [random.randint(0, 100000000000) for x in range(10)]


def get_report() -> int:
    """
    Function used in examples to show how you can mock functions.

    This 'get_report' function mimics a function that reaches
    out to a database to get some data. Then it performs calculations
    on that data and returns the result.

    What it 'really' does is:
    - call 'get_database_data' which:
      - sleeps for 5 seconds
      - returns a list of random integers
    - sum all integers in the list
    - divide the sum by the length of the list
    - return the result
    """

    # get the counters from a database:
    data = get_database_data()

    # perform 'complex' calculations:
    average = sum(data) // len(data)
    return average


if __name__ == "__main__":
    print(get_report())
