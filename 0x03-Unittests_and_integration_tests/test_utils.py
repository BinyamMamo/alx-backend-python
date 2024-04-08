#!/usr/bin/env python3
"""
Task 0. Parameterize a unit test
Write the first unit test for utils.access_nested_map
"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Class for testing access_nested_map utility."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nest, path):
        """Test access_nested_map raises KeyError for invalid paths."""
        with self.assertRaises(KeyError):
            access_nested_map(nest, path)


class TestGetJson(unittest.TestCase):
    """Class for testing get_json utility."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        Test get_json utility.

        Args:
            url: URL to fetch JSON from.
            payload: Expected JSON payload.
        """

        class Mocked(Mock):
            """Mocked response object."""

            def json(self):
                """Return mock JSON payload."""
                return payload

        with patch("requests.get") as MockClass:
            """Mock requests.get call."""
            MockClass.return_value = Mocked()
            self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """TestMemoize tests memoize decorator"""

    def test_memoize(self):
        """test_memoize tests memoized functions are only called once"""

        class TestClass:
            """TestClass is a class for testing memoize"""

            def a_method(self):
                """a_method returns a constant"""
                return 42

            @memoize
            def a_property(self):
                """a_property returns result of a_method memoized"""
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mocked:
            spec = TestClass()
            spec.a_property
            spec.a_property
            mocked.asset_called_once()
