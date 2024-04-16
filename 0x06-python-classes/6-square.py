#!/usr/bin/python3
"""A module designated for creating and initializing squares"""


class Square:
    """A Class that creates a square with a given size"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the class
        Attributes:
            size: size of the square to be initialized"""
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        err = False
        if type(value) is not tuple or len(value) != 2:
            err = True
        else:
            for i in value:
                if type(i) is not int or i < 0:
                    err = True
                    break
        if err:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints a square with # representation"""
        if self.__size == 0:
            print()
            return
        print("\n"*self.__position[1], end="")
        for i in range(self.__size):
            print(" "*self.__position[0], end="")
            for j in range(self.__size):
                print("#", end="")
            print()
