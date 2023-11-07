#!/usr/bin/python3
'''queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit'''
import requests


def number_of_subscribers(subreddit):
    ''' this function counts the numbr of subscribers in a
    subreddit using API calls'''

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36'}

    url = 'https://www.reddit.com/r/{}/about.json' \
          .format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    return response.json().get('data').get("subscribers")
