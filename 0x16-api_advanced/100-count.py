#!/usr/bin/python3
'''return all hot posts listed for a given subreddit'''
import requests


def count_words(subreddit, word_list, after=None, count={}):
    ''' returns all hot posts listed for a given subreddit.'''

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36'}

    params = {'limit': 10, 'after': after}

    url = 'https://www.reddit.com/r/{}/hot.json' \
          .format(subreddit)

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 404:
        return
    results = response.json()
    # print(response.url)
    word_list = [x.lower() for x in word_list]

    if results.get('data'):
        for item in results.get('data').get("children"):
            title = item.get('data').get('title')

            for word in title.split():
                word = word.lower()
                if word in word_list:
                    count[word] = count.get(word, 0) + 1

        after = results.get('data').get('after')
        # print(count, after)

    if after is not None:
        count_words(subreddit, word_list, after, count)
    else:
        for k, v in sorted(count.items(), key=lambda x: (x[1], x[0])):
            print('{}: {}'. format(k, v))
        return
