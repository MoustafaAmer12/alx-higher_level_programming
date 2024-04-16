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
        count = 0
        try:
            for i in value:
                count += 1
                if type(i) is not int:
                    err = True
                elif i < 0:
                    err = True
        except Exception:
            err = True
        if count != 2:
            err = True
        if err:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """Prints a square with # representation"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            for j in range(self.position[0]):
                print(" ", end="")
            for j in range(self.size):
                print("#", end="")
            print()
