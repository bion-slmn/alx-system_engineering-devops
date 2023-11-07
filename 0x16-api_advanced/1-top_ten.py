#!/usr/bin/python3
'''prints titles of the first 10 hot posts listed for a given subreddit'''
import requests


def top_ten(subreddit):
    ''' prints titles of first 10 hot posts listed for a given subreddit.'''

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36'}

    params = {'limit': 10}

    url = 'https://www.reddit.com/r/{}/hot.json' \
          .format(subreddit)

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get('data').get("children")
    for item in results:
        print(item.get('data').get('title'))
