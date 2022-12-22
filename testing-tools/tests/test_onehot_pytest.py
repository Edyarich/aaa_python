"""Unit tests for one_hot_encoder.py"""
import os
import sys
import pytest


currentdir = os.path.dirname(os.path.abspath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import one_hot_encoder as ohe


def test_empty():
    """Test exception raising"""
    with pytest.raises(TypeError):
        ohe.fit_transform()


def test_single_example():
    """Test embedding of single string"""
    value = ['apple']
    expected_result = [('apple', [1])]
    encoded_value = ohe.fit_transform(value)
    assert encoded_value == expected_result


def test_similar():
    """Test embedding of single string, repeated n times"""
    values = ['apple'] * 10
    expected_result = [('apple', [1])] * 10
    encoded_values = ohe.fit_transform(values)
    assert encoded_values == expected_result


def test_normal():
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
    assert encoded_colors == expected_result
