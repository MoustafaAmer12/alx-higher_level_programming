#!/usr/bin/python3
"""A Module that creates and identifies user defined squares with sizes"""


class Square:
    """A class for creating squares with specific sizes"""
    def __init__(self, size=0):
        """Constructor for the class
        Attributes:
            size: size of the square to be initialized"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
