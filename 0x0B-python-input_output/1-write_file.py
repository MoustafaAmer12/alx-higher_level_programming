#!/usr/bin/python3
"""
A Module that defines a function to write
a given string of data into a file
"""


def write_file(filename="", text=""):
    """ A function that writes a text into
    a file.
    Returns:
        number of characters written
    """
    size = 0
    with open(filename, "w", encoding="utf-8") as file:
        size = file.write(text)
    return size
