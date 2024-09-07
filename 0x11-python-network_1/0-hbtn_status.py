#!/usr/bin/python3
""" Write a Python script that fetches
    https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import urllib.request

    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as res:

        byte_v = res.read()
        typ = type(byte_v)
        utf_v = byte_v.decode('utf-8')

        print("""Body response:
\t- type: {}
\t- content: {}
\t- utf8 content: {}""".format(typ, byte_v, utf_v))
