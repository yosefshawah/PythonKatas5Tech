import unittest
from unittest.mock import patch, Mock
from katas.github_user_fetcher import fetch_github_user, get_user_repositories_count


class TestGitHubUserFetcher(unittest.TestCase):
    
    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_user_success(self, mock_get):
        # Mock successful API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'login': 'octocat',
            'name': 'The Octocat',
            'public_repos': 8,
            'followers': 9999
        }
        mock_get.return_value = mock_response
        
        result = fetch_github_user('octocat')
        expected = {'login': 'octocat', 'name': 'The Octocat', 'public_repos': 8, 'followers': 9999}
        self.assertEqual(result, expected)
    
    @patch('katas.github_user_fetcher.requests.get')
    def test_fetch_user_not_found(self, mock_get):
        # Mock 404 response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = fetch_github_user('nonexistentuser')
        self.assertIsNone(result)
    
    def test_get_repositories_count(self):
        with patch('katas.github_user_fetcher.fetch_github_user') as mock_fetch:
            # Test successful case
            mock_fetch.return_value = {'public_repos': 42}
            result = get_user_repositories_count('testuser')
            self.assertEqual(result, 42)
            
            # Test when user not found
            mock_fetch.return_value = None
            result = get_user_repositories_count('baduser')
            self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
