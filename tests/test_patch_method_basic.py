"""
python -m pytest .\tests\test_patch_method_basic.py
"""
from src.generate_database_report_method import ReportGenerator
from unittest import mock


@mock.patch("src.generate_database_report_method.ReportGenerator._get_database_data")
def test_report_generator(mocked_get_database_data):
    """
    Test that the 'generate_report' method returns the expected value.
    """
    mocked_get_database_data.return_value = [
        10,
        10,
    ]
    report_generator = ReportGenerator()
    assert report_generator.generate_report() == 10
