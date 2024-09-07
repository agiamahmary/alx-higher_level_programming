#!/usr/bin/python3
"""Write a Python script that takes in a letter and
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    r = requests.get(url)

    if len(sys.argv) == 1:
        data = {'q': ""}
    else:
        data = {'q': sys.argv[1]}

    r = requests.post(url, data)

    try:
        data = r.json()

        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except ValueError:
        print("Not a valid JSON")
