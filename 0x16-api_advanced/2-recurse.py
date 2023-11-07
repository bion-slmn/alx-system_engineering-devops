#!/usr/bin/python3
'''return all hot posts listed for a given subreddit'''
import requests


def recurse(subreddit, after=None, hotlist=[]):
    ''' returns all hot posts listed for a given subreddit.'''

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36'}

    params = {'limit': 100, 'after': after}

    url = 'https://www.reddit.com/r/{}/hot.json' \
          .format(subreddit)

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json()

    for item in results.get('data').get("children"):
        hotlist.append(item.get('data').get('title'))

    after = results.get('data').get('after')

    if after:
        recurse(subreddit, after, hotlist)
    return hotlist
