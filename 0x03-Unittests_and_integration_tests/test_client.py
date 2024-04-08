#!/usr/bin/env python3
"""
Tasks 4 - 9
Tests for client.py
"""

import unittest
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from urllib import response


class TestGithubOrgClient(unittest.TestCase):
    """
    Test class for GithubOrgClient
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, data, mock):
        """
        Test org method
        """
        endpoint = 'https://api.github.com/orgs/{}'.format(data)
        spec = GithubOrgClient(data)
        spec.org()
        mock.assert_called_once_with(endpoint)

    @parameterized.expand([
        ('random_url', {'repos_url': 'http://some_url.com'})
    ])
    def test_public_repos_url(self, name, result):
        """
        Test public_repos_url property
        """
        with patch('client.GithubOrgClient.org',
                   PropertyMock(return_value=result)):
            response = GithubOrgClient(name)._public_repos_url
            self.assertEqual(response, result.get('repos_url'))

    @patch('client.get_json')
    def test_public_repos(self, mocked_method):
        """
        Test public_repos method
        """
        payload = [{"name": "Google"}, {"name": "TT"}]
        mocked_method.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public:

            mocked_public.return_value = "world"
            response = GithubOrgClient('test').public_repos()

            self.assertEqual(response, ["Google", "TT"])

            mocked_public.assert_called_once()
            mocked_method.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, key, expectation):
        """
        Test has_license method
        """
        result = GithubOrgClient.has_license(repo, key)
        self.assertEqual(result, expectation)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient integration"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures"""
        cls.get_patcher = patch('requests.get', side_effect=[
            cls.org_payload, cls.repos_payload
        ])
        cls.mocked_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class fixtures"""
        cls.get_patcher.stop()

    @patch('client.get_json')
    def test_public_repos(self, mocked_get_json):
        """tests public repos"""
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:
            expected_payload = [{"name": "Repo1"}, {"name": "Repo2"}]
            mocked_get_json.return_value = expected_payload

            org_client = GithubOrgClient('myorg')
            repos = org_client.public_repos()

            mocked_public_repos_url.assert_called_once()
            mocked_get_json.assert_called_once()

            self.assertEqual(repos, expected_payload)

    @patch('client.get_json')
    def test_public_repos_with_license(self, mocked_get_json):
        """
        Test public repos with license
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mocked_public_repos_url:
            expected_payload = [
                {"name": "Repo1", "license": {"key": "apache-2.0"}},
                {"name": "Repo2", "license": {"key": "apache-2.0"}}
            ]
            mocked_get_json.return_value = expected_payload

            org_client = GithubOrgClient('myorg')
            repos = org_client.public_repos(license="apache-2.0")

            mocked_public_repos_url.assert_called_once()
            mocked_get_json.assert_called_once()

            self.assertEqual(repos, expected_payload)


if __name__ == '__main__':
    unittest.main()
