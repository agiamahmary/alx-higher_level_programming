#!/usr/bin/python3
"""Modlue contains rectangle class"""
from .base import Base


class Rectangle(Base):
    ''' Rectangle class '''
    def __init__(self, width, height, x=0, y=0, id=None):
        """Init Method"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(self.__width))
        if(value <= 0):
            raise ValueError("{} must be > 0".format(self.__width))
        self.__width = value

    @property
    def height(self):
        '''Getter for height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Setter for height'''
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(self.__height))
        if(value <= 0):
            raise ValueError("{} must be > 0".format(self.__height))
        self.__height = value

    @property
    def x(self):
        '''Getter for x'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Setter for x'''
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(self.__x))
        if(value < 0):
            raise ValueError("{} must be >= 0".format(self.__x))
        self.__x = value

    @property
    def y(self):
        '''Getter for y'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Setter for y'''
        if (value.__class__ != int):
            raise TypeError("{} must be an integer".format(self.__y))
        if(value < 0):
            raise ValueError("{} must be >= 0".format(self.__y))
        self.__y = value
