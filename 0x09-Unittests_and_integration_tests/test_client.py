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

    def test_public_repos_url(self):
        """
        Using patch context manager to patch and return
        a known payload.
        """
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mocking:
            mocking.return_value = {"repos_url": "World"}
            test_obj = GithubOrgClient("test")
            self.assertEqual(test_obj._public_repos_url, "World")


if __name__ == '__main__':
    unittest.main()
