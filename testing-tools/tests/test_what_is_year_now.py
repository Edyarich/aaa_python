"""Tests for what_is_year_now.py"""
import os
import sys
import unittest
import time
from unittest.mock import patch, MagicMock


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import what_is_year_now as wiyn


REQUEST_DELAY = 3

class TestWIYN(unittest.TestCase):
    """Test function what_is_year_now"""
    @patch('what_is_year_now.json.load')
    def test_dmy_format(self, json_dict: MagicMock) -> None:
        """Test the correct work with DD.MM.YYYY date format"""
        json_dict.return_value = {"datetime": "17.11.1999"}
        time.sleep(REQUEST_DELAY)
        response = wiyn.what_is_year_now()
        self.assertEqual(response, 1999)

    @patch('what_is_year_now.json.load')
    def test_ymd_format(self, json_dict: MagicMock) -> None:
        """Test the correct work with YYYY-MM-DD date format"""
        json_dict.return_value = {"datetime": "1999-11-17"}
        time.sleep(REQUEST_DELAY)
        response = wiyn.what_is_year_now()
        self.assertEqual(response, 1999)

    @patch('what_is_year_now.json.load')
    def test_exception_raising(self, json_dict: MagicMock) -> None:
        """Check exception raising for any other date format"""
        json_dict.return_value = {"datetime": "17.11..1999"}
        time.sleep(REQUEST_DELAY)
        self.assertRaises(ValueError, wiyn.what_is_year_now)
