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


class TestGetJson(unittest.TestCase):
    """
    Test class for json calls.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """
        This method tests utils.get_json
        """
        patch_obj = patch("requests.get",
                          **{"return_value.json.return_value": payload})

        mock = patch_obj.start()
        self.assertEqual(get_json(url), payload)
        mock.assert_called_once()
        patch_obj.stop()


class TestMemoize(unittest.TestCase):
    """
    Testing class for Memoize.
    """

    def test_memoize():
        """
        Memoize test method.
        """
        class TestClass:
            """
            TestClass definition.
            """
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_cls = TestClass()
            test_cls.a_property
            test_cls.a_property
            mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
