#!/usr/bin/python3
""" Contains class Mylist """


class MyList(list):
    ''' Child of list base class '''

    def print_sorted(self):
        """ Print mylist in ascending order """
 
        print(sorted(self))
