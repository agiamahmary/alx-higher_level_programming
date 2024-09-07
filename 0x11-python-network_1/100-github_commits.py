#!/usr/bin/python3
"""
Write a Python script that takes 2 arguments in
order to solve this challenge

CHALLENGE: Please list 10 commits (from the most recent to oldest)
of the repository rails by the user rails
"""

if __name__ == "__main__":
    import requests
    import sys

    owner = sys.argv[1]
    repo = sys.argv[2]

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    commits = r.json()

    for commit in commits[:10]:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
