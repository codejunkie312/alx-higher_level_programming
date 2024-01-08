#!/usr/bin/python3
"""script that takes in a URL and an email address,
sends a 'POST' request to the passed URL with the email as a parameter,
and finally displays the body of the response."""
import requests
import sys


def send_post_request(url, email):
    """send post request"""
    data = {'email': email}
    response = requests.post(url, data=data)
    return response.text


if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    response_body = send_post_request(url, email)
    print(response_body)
