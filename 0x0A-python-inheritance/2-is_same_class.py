#!/usr/bin/python3
“”” Contains function is_same_class
    - that returns true the exact instance
    of a_class.
“””


def is_same_class(obj, a_class):
    """ Returns true is obj is exact instance of a_class """
    
    return obj.__class__ == a_class
