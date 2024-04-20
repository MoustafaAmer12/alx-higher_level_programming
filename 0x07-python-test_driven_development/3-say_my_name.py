#!/usr/bin/python3
"""
Module That has a function that lists the full name
say_my_name: prints the full name
of given parameters
"""


def say_my_name(first_name, last_name=""):
    """Prints the full name of the given arguments
    Returns:
        None"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
