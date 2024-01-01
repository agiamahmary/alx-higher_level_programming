#!/usr/bin/python3
""" Contains a BaseGeometry class """

class BaseGeometry:
    """ METHOD  """
    
    def area(self):
        """  Raise exception that area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates if value is an integer else raise an exception """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
