"""Tests for what_is_year_now.py"""
import os
import sys
import unittest
from unittest.mock import patch, MagicMock


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import what_is_year_now as wiyn


class TestWIYN(unittest.TestCase):
    """Test function what_is_year_now"""
    @patch('urllib.request.urlopen')
    def test_dmy_format(self, mock_urlopen: MagicMock) -> None:
        """Test the correct work with DD.MM.YYYY date format"""
        mock = MagicMock()
        mock.read.return_value = """{
            "datetime": "17.11.1999"
        }"""
        mock.__enter__.return_value = mock
        mock_urlopen.return_value = mock

        self.assertEqual(wiyn.what_is_year_now(), 1999)

    @patch('urllib.request.urlopen')
    def test_ymd_format(self, mock_urlopen: MagicMock) -> None:
        """Test the correct work with YYYY-MM-DD date format"""
        mock = MagicMock()
        mock.read.return_value = """{
            "datetime": "1999-11-17"
        }"""
        mock.__enter__.return_value = mock
        mock_urlopen.return_value = mock

        self.assertEqual(wiyn.what_is_year_now(), 1999)

    @patch('urllib.request.urlopen')
    def test_exception_raising(self, mock_urlopen: MagicMock) -> None:
        """Check exception raising for any other date format"""
        mock = MagicMock()
        mock.read.return_value = """{
            "datetime": "17.11..1999"
        }"""
        mock.__enter__.return_value = mock
        mock_urlopen.return_value = mock

        self.assertRaises(ValueError, wiyn.what_is_year_now)
