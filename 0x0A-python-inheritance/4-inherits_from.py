#!/usr/bin/python3
""" Contains function inherits_from(obj, a_class)

-that returns true if object is an instance of
a class that inherited directly
or indirectly from the specified class
"""


def inherits_from(obj, a_class):
    """ Return True if object returns true if its an instance of a_class """
    return issubclass(obj.__class__, a_class) and obj.__class__ != a_class
