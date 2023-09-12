#!/usr/bin/python3
"""
contains the MyList class - A subclass of list 
"""


class MyList(list):
    """a subclass of list"""
    def __init__(self):
        """initializes the object using the baseClass init method"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list first calling sorted func"""
        print(sorted(self))
