#!/usr/bin/python3
"""
A Module that defines a function to
read a text file
"""


def read_file(filename=""):
    """A function that reads a file using the utf-8
    encoding and prints the data in the file.
    """
    f_data = ""
    with open(filename, encoding="utf-8") as file:
        f_data = file.read()
    print(f_data, end="")
