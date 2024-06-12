#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

from sys import argv
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, return 0.
    """
    req = requests.get(
        "https://www.reddit.com/r/{}/about.json".format(subreddit),
        headers={"User-Agent": "Custom"}
    )

    if req.status_code == 200:
        if(not req.json().get("data").get("subscribers")):
            return 0
        return req.json().get("data").get("subscribers")
    else:
        return 0
def main(*args):
    """
    Main function
    """
    if len(args) < 1:
        print("Please pass an argument for the subreddit.")
        return 1
    return number_of_subscribers(args[1])

if __name__ == "__main__":
    print(main(*argv))
