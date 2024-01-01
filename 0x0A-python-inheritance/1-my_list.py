#!/usr/bin/python3
""" Contains class Mylist """


class Mylist(list):
    """ Inherits superclass list
    Args:
       list: parent classs
    """

    def print_sorted(self):
        """ Print mylist in ascending order """
        sorted_list = sorted(self)
        print(sorted_list)
