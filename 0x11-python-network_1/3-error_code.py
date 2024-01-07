#!/usr/bin/python3
""" script that takes in a URL,
sends a request to the URL
and displays the body of the response (decoded in 'utf-8')"""
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """Fetches URL content"""
    try:
        with urllib.request.urlopen(url) as response:
            response_body = response.read().decode('utf-8')
            return response_body
    except urllib.error.HTTPError as e:
        return 'Error code: {}'.format(e.code)


if __name__ == '__main__':
    url = sys.argv[1]

    result = fetch_url_content(url)
    print(result)
