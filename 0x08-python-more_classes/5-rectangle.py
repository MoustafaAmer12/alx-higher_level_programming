#!/usr/bin/python3
"""
Module that identifies a Rectangle class
class:
    Rectangle
"""


class Rectangle:
    """
    A class that initializes rectangles
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 0 if self.width == 0 or self.height == 0\
                    else 2 * (self.width + self.height)

    def __str__(self):
        rect = ""
        if self.width == 0 or self.height == 0:
            return rect
        for i in range(self.height):
            rect += "#" * self.width
            if i != self.height - 1:
                rect += "\n"
        return rect

    def __repr__(self):
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        print("Bye rectangle...")
