#!/usr/bin/python3
"""A module designated for creating and initializing squares"""


class Square:
    """A Class that creates a square with a given size"""
    def __init__(self, size=None):
        """Constructor of the class
        Attributes:
            size: size of the square to be initialized"""
        self.__size = size
