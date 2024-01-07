#!/usr/bin/python3
"""script that takes in a URL,
sends a request to the URL and
displays the value of the variable X-Request-Id in the response header"""
import requests
import sys


def fetch_x_request(url):
    """fetches the value of X-Request-Id from URL response body"""
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    return x_request_id


if __name__ == '__main__':
    url = sys.argv[1]

    x_request_id = fetch_x_request(url)
    print(x_request_id)
