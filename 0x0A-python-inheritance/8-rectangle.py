#!/usr/bin/python3
""" Contains Rectangle class

"""


Rectangle(BaseGeometry):
    """ Inherits from BaseGeometry """
    def __init__(self, width, height):
        if not self.integer_validator('width', width):
            if  not self.integer_validator("height", height):
                self.__height = height
                self.__width = width
