#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def fetch_url_content(url):
    """fetches URL content"""
    response = requests.get(url)

    print("Body response:")
    print('\t- type: {}'.format(type(response.text)))
    print('\t- content: {}'.format(response.text))


if __name__ == '__main__':
    url = "https://alx-intranet.hbtn.io/status"
    fetch_url_content(url)
