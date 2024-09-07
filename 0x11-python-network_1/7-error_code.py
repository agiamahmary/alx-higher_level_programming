#!/usr/bin/python3
"""Write a Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    try:
        r = requests.get(url)
        if r.status_code >= 400:
            r.raise_for_status()
        else:
            print(r.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
