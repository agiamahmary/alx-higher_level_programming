#!/usr/bin/python3
"""Module with Base class"""


class Base:
    """Base Class"""
    __nb_objects = 0
    def __init__(self, id=None):
        '''init Method'''
        if (id != None):
            self.id = id
        else:
             __nb_objects += 1
            self.id = id
