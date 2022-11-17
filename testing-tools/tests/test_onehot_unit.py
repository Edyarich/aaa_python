"""Unit tests for one_hot_encoder.py"""
import os
import sys
import unittest


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import one_hot_encoder as ohe


class TestOHE(unittest.TestCase):
    """Test one-hot-encoding implementation"""
    def test_empty(self):
        """Test exception raising"""
        self.assertRaises(TypeError, ohe.fit_transform)

    def test_single_example(self):
        """Test embedding of single string"""
        value = ['apple']
        expected_result = [('apple', [1])]
        encoded_value = ohe.fit_transform(value)
        self.assertEqual(encoded_value, expected_result)

    def test_similar(self):
        """Test embedding of single string, repeated n times"""
        values = ['apple'] * 10
        expected_result = [('apple', [1])] * 10
        encoded_values = ohe.fit_transform(values)
        self.assertEqual(encoded_values, expected_result)

    def test_normal(self):
        """Simple test"""
        colors = ['red', 'blue', 'red', 'green', 'green', 'blue', 'blue', 'red']
        encoded_colors = ohe.fit_transform(colors)
        expected_result = [
            ('red', [0, 0, 1]),
            ('blue', [0, 1, 0]),
            ('red', [0, 0, 1]),
            ('green', [1, 0, 0]),
            ('green', [1, 0, 0]),
            ('blue', [0, 1, 0]),
            ('blue', [0, 1, 0]),
            ('red', [0, 0, 1]),
        ]
        self.assertTrue(encoded_colors == expected_result)


if __name__ == '__main__':
    unittest.main()
