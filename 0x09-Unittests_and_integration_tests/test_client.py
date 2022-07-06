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
        """
        This is the test_org documentation
        """
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

    @patch('client.get_json')
    def test_public_repos(self, json_mock):
        """
        Test that the list of repos is what
        you expect from the chosen payload.
        """
        payload = [
            {"name": "Twitter"},
            {"name": "Google"}
        ]

        json_mock.return_value = payload

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mocking:

            mocking.return_value = "help"
            test_obj = GithubOrgClient("test")
            res = test_obj.public_repos()

            self.assertEqual(res, [dic["name"] for dic in payload])

            mocking.assert_called_once()
            json_mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, rep, lic_key, expected_result):
        """
        Method for testing licenses.
        """

        res = GithubOrgClient.has_license(rep, lic_key)
        self.assertEqual(expected_result, res)


if __name__ == '__main__':
    unittest.main()
