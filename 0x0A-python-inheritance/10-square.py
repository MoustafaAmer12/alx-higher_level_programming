#!/usr/bin/python3
"""A Module that declares a square class
that inherits from the rectangle class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
