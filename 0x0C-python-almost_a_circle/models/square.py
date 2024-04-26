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

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/\
{self.y} - {self.height}"
