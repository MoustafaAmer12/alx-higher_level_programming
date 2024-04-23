#!/usr/bin/python3
"""A Module that defines a rectangle class
inherits from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A Rectangle Class that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """Initializes objects of the class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
