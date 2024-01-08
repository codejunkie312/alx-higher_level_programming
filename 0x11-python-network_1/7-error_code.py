#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the body of the response."""
import requests
import sys


def fetch_url_content(url):
    """fetchs URL content and handles Errors if met"""
    response = requests.get(url)
    if response.status_code >= 400:
        return 'Error code: {}'.format(response.status_code)
    else:
        return response.text


if __name__ == '__main__':
    url = sys.argv[1]
    response = fetch_url_content(url)
    print(response)
