#!/usr/bin/python3
"""A modlue that contains read_file func. """


def read_file(filename=""):
    """ A func that prints content of a txt file """
    with open(filename, 'r', encoding='utf-8') as f:
        print(r.read())
