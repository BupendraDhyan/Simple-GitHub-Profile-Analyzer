import requests

def analyze_github_profile(username):
    # Make a GET request to the GitHub API to fetch user information
 response = requests.get(f"https://api.github.com/users/{username}")
    
    if response.status_code == 200:
        user_data = response.json()