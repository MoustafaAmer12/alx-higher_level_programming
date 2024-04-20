#!/usr/bin/python3
"""
Module that prints a square in the form of #
print_square:
    Prints the square in the form of # given its size
"""


def print_square(size):
    """Prints the square in the form of #
    Returns:
        None
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        print("#"*size, end="")
        print()
