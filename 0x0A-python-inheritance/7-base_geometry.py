#!/usr/bin/python3
"""
A Module that declares a base geometry class
"""


class BaseGeometry:
    """
    A Class that calculates the area
    """
    def area(self):
        """
        Raises Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates integer values of the class
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
