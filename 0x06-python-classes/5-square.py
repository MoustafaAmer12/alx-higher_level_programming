#!/usr/bin/python3
"""A module designated for creating and initializing squares"""


class Square:
    """A Class that creates a square with a given size"""
    def __init__(self, size=0):
        """Constructor for the class
        Attributes:
            size: size of the square to be initialized"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square
        Returns:
            Area"""
        return pow(self.__size, 2)

    def my_print(self):
        """Prints a square with # representation"""
        for i in range(self.size):
            for j in range(self.size):
                print("#", end="")
            if i != self.size - 1:
                print()
        print()
