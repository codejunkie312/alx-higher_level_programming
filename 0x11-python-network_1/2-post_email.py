#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a 'POST' request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in 'utf-8')"""
import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    """Send the POST request"""
    data = urllib.parse.urlencode({'email': email})
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as response:
        response_body = response.read().decode('utf-8')
        return response_body


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
