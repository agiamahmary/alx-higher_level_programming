#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

if __name__ == "__main__":
    import requests
    import sys
    from requests.auth import HTTPBasicAuth

    user = sys.argv[1]
    passwd = sys.argv[2]

    auth = HTTPBasicAuth(user, passwd)
    url = "https://api.github.com/user"

    r = requests.get(url, auth=auth)

    print(r.json().get("id"))
