#!/usr/bin/python3
""" Contains class Mylist """


class Mylist(list):
    """ A class that mimics most 
        of the opearations form superclass list
    """
    def print_sorted(self):
         """ Print mylist in ascending order """
         return self.sort()
