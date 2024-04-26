#!/usr/bin/python3
"""
A Module that defines a rectangle class
inherits from Base Class
"""
from models import base
Base = base.Base


class Rectangle(Base):
    """Rectangle Class

    Description:
        A Class that inherits from base class to
        define a rectangle

    Attributes:
        private inst attribute width
        private inst attribute height
        private inst attribute x
        private inst attribute y

    Methods:
        __init__ : Class Constructor
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __getattr__(self, name):
        if name == "id":
            return super().__getattr__(name)
        if name in ["x", "y", "width", "height"]:
            return self.__dict__[f"_{self.__class__.__name__}__{name}"]
        return self.__dict__[f"{name}"]

    def __setattr__(self, name, value):
        if name == "id":
            super().__setattr__(name, value)
        elif name in ["x", "y", "width", "height"]:
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if (name == "width" or name == "height") and value <= 0:
                raise ValueError(f"{name} must be > 0")
            if (name == "x" or name == "y") and value < 0:
                raise ValueError(f"{name} must be >= 0")
            self.__dict__[f"_{self.__class__.__name__}__{name}"] = value
        else:
            self.__dict__[f"{name}"] = value

    def area(self):
        """Function that calculates the area of
        the retangle
        Returns:
            Area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """Function that prints the recangle in
        the form of #
        """
        string = "\n" * self.y
        rect = " " * self.x
        rect += "#" * self.width
        for j in range(self.height):
            string += rect
            if j != self.height - 1:
                string += "\n"
        print(string)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
