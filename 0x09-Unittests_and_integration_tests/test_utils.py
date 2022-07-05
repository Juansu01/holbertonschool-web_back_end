#!/usr/bin/env python3
"""
Unnitests module.
"""

import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """
    Testing class for access nested map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        test that the method returns what it is supposed to
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that a KeyError is raised for the following inputs
        """

        with self.assertRaises(KeyError) as exc:
            access_nested_map(nested_map, path)
            self.assertEqual(f"KeyError('{expected}')", repr(exc.exception))
