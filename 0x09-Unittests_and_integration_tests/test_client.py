#!/usr/bin/env python3
"""
Unnitests module.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock, Mock
import json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    Testing class for Github Org Client
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, name, mock):
        test_cl = GithubOrgClient(name)
        self.assertEqual(test_cl.org, mock.return_value)
        mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
