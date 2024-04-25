#!/usr/bin/python3
"""
A Module that defines a function to
read a text file
"""


def read_file(filename=""):
    f_data = ""
    with open(filename, encoding="utf-8") as file:
        f_data = file.read()
    print(f_data, end="")
