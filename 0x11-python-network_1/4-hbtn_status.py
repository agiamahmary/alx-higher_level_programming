#!/usr/bin/python3
"""Write a Python script that fetches
    https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    r = requests.get('https://alx-intranet.hbtn.io/status')

    r = r.text
    typ = type(r)

    print("""Body response:
\t- type: {}
\t- content: {}""".format(typ, r))
