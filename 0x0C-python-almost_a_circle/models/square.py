#!/usr/bin/python3
"""Module contains square class"""
from .rectangle import Rectangle


class Square:
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """ Init method """
        super().__init__(self, size, x=0, y=0, id)
        
    def __str__(self):
        """ str method """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
