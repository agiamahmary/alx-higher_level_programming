#!/usr/bin/python3
""" Contains function `is_kind_of_class`

-that returns true if 
object is the exact or `indirect` instance
of the specified class 
"""
def is_kind_of_class(obj, a_class):
    """ Return true if obj is a direct or indirect instance of a_class """

    return isinstance(obj, a_class)
