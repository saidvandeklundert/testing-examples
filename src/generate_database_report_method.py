import time
import random
from typing import List


class ReportGenerator:
    """
    Class that generates traffic reports.
    """

    def generate_report(self) -> int:
        data = self._get_database_data()

        average = sum(data) // len(data)
        return average

    @staticmethod
    def _get_database_data() -> List[int]:
        """
        - sleeps for 5 seconds
        - returns a list of random integers
        """
        time.sleep(5)
        return [random.randint(0, 100000000000) for _ in range(10)]
