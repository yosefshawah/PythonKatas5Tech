import requests
from typing import Dict, Optional

# Note
# The unittest for this kata *must mock* the request to GitHub API


def fetch_github_user(username: str) -> Optional[Dict]:
    """
    Fetches user information from GitHub API.
    
    Args:
        username: GitHub username to fetch
        
    Returns:
        Dictionary containing user info with keys: 'login', 'name', 'public_repos', 'followers'
        Returns None if user not found or API error occurs
        
    Example:
        user_info = fetch_github_user("octocat")
        # Should return: {
        #     'login': 'octocat',
        #     'name': 'The Octocat', 
        #     'public_repos': 8,
        #     'followers': 9999
        # }
    """
    try:
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            return {
                'login': data.get('login'),
                'name': data.get('name'),
                'public_repos': data.get('public_repos'),
                'followers': data.get('followers')
            }
        else:
            return None
    except Exception:
        return None


def get_user_repositories_count(username: str) -> int:
    """
    Gets the number of public repositories for a GitHub user.
    
    Args:
        username: GitHub username
        
    Returns:
        Number of public repositories, or 0 if user not found/error
    """
    user_info = fetch_github_user(username)
    if user_info and user_info.get('public_repos') is not None:
        return user_info['public_repos']
    return 0


if __name__ == '__main__':
    # Test the functions
    user = fetch_github_user("octocat")
    print(f"User info: {user}")
    
    repo_count = get_user_repositories_count("octocat")
    print(f"Repository count: {repo_count}")
