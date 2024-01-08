#!/usr/bin/python3
"""A python script that lists 10 commits of a 'repo' by 'owner'."""
import sys
import requests


def get_commits(repo, owner):
    """fetchs commits."""
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    commits = response.json()
    try:
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit.get('commit').get('author').get('name')
            print(f'{sha}: {author}')
    except IndexError:
        pass


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]

    get_commits(repo, owner)
