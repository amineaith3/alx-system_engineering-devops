#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests

def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0.0 (by /u/Significant-Bug9944)"}
    
    try:
        req = requests.get(url, headers=headers, allow_redirects=False)
        if req.status_code == 200:
            return req.json().get("data", {}).get("subscribers", 0)
        else:
            return 0
    except requests.RequestException:
        return 0
