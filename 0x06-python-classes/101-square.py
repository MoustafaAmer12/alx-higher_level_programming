#!/usr/bin/python3
"""A Module that creates and prints a square"""


class Square:
    """A Class that creates a square with a given size"""
    def __init__(self, size=0, position=(0, 0)):
        """Constructor for the class
        Attributes:
            size: size of the square to be initialized"""
        self.size = size
        self.position = position

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

    def area(self):
        """Calculates the area of the square
        Returns:
            Area"""
        return self.size**2

    def my_print(self):
        """Prints a square with # representation"""
        if self.size == 0:
            print()
            return
        print("\n"*self.position[1], end="")
        for i in range(self.size):
            print(" "*self.position[0], end="")
            for j in range(self.size):
                print("#", end="")
            print()

    def __str__(self):
        string = ""
        if self.size == 0:
            string += "\n"
        else:
            string += "\n"*self.position[1]
            for i in range(self.size):
                string += " "*self.position[0]
                string += "#"*self.size
                if i != self.size - 1:
                    string += "\n"
        return string
