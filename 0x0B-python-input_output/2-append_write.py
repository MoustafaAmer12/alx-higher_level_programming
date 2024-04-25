#!/usr/bin/python3
"""
A Module that defines a function that
appends a given text to a file
"""


def append_write(filename="", text=""):
    """A function that appends data to a given
    text file.
    Returns:
        number of characters appended to the file
    """
    size = 0
    with open(filename, "a", encoding="utf-8") as file:
        size = file.write(text)
    return size
