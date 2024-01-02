#!/usr/bin/python3
""" Contains a BaseGeometry class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Inherits BaseGeometry """

    def __init__(self, width, height):
        ''' init method '''
        self.integer_validator('width', width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
