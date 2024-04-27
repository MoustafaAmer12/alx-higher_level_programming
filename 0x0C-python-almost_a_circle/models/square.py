#!/usr/bin/python3
"""
Module that creates a Square Class that
inherits from the Rectangle Class and
overrides its related methods
"""
from models import rectangle
Rectangle = rectangle.Rectangle


class Square(Rectangle):
    """Square Class

    Description:
        Class that defines a Square object
        blueprint for creating and adjusting a Square
        instance utilizing its relation to Rectangle Class.

    Attributes:
        private instance attribute: size
        private instance attribute: x
        private instance attribute: y
        public instance attribute: id

    Methods:
        __init__: Class Constructor
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __getattr__(self, name):
        if name == "size":
            return self.width
        return super().__getattr__(name)

    def __setattr__(self, name, value):
        if name == "size":
            self.width = value
            self.height = value
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """A method that updates the attributes
        of an Square instance
        """
        if args and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.size = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                self.__dict__[key] = value
