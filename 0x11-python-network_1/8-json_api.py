#!/usr/bin/python3
"""script that takes in a letter
and sends a POST request to 'http://0.0.0.0:5000/search_user'
with the letter as a parameter."""
import requests
import sys


def search_user(url, query):
    """searches for user"""
    response = requests.post(url, data={'q': query})
    try:
        json_response = response.json()
        if json_response:
            return '[{}] {}'.format(json_response['id'], json_response['name'])
        else:
            return "No result"
    except ValueError:
        return "Not a valid JSON"


if __name__ == '__main__':
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    result = search_user(url, query)
    print(result)
