#!/usr/bin/env python3
"""
Task 0. Parameterize a unit test
Write the first unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized, parameterized_class
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map utility."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nest, path, value):
        """
        Test access_nested_map utility.

        Args:
            nest: Nested dictionary.
            path: Path to access in nested dictionary.
            value: Expected value.
        """
        self.assertEqual(access_nested_map(nest, path), value)
