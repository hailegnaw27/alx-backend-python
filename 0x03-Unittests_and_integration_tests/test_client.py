#!/usr/bin/env python3
"""Unit tests for the GithubOrgClient class"""

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for the GithubOrgClient class"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test the org method with different organization names"""
        client = GithubOrgClient(org_name)
        client.org()
        mock_get_json.assert_called_once_with(client.ORG_URL.format(org=org_name))

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            payload = {"repos_url": "https://api.github.com/orgs/test/repos"}
            mock_org.return_value = payload
            client = GithubOrgClient('test')
            result = client._public_repos_url
            self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/test/repos"
            client = GithubOrgClient('test')
            result = client.public_repos()

            expected = [item["name"] for item in payload]
            self.assertEqual(result, expected)

            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class using fixtures"""

    @classmethod
    def setUpClass(cls):
        """Set up the class with patched requests.get"""
        config = {'return_value.json.side_effect': [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload
        ]}
        cls.get_patcher = patch('requests.get', **config)
        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """Integration test for the public_repos method"""
        client = GithubOrgClient("google")

        self.assertEqual(client.org, self.org_payload)
        self.assertEqual(client.repos_payload, self.repos_payload)
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """Integration test for the public_repos method with a specific license"""
        client = GithubOrgClient("google")

        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("XLICENSE"), [])
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down the class by stopping the patcher"""
        cls.get_patcher.stop()
