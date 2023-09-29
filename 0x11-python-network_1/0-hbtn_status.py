#!/usr/bin/python3
'''  Python script that fetches https://alx-intranet.hbtn.io/status
using python urllib'''
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        response = r.read()
        print(f'''Body response:
    -type: {type(response)}
    -content: {response}
    -utf8 content: {response.decode('utf-8')}''')
