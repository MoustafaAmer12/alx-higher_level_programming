#!/usr/bin/python3
"""A Module that defines a subclass of the
python built-in list class
"""


class MyList(list):
    """
    A class that prints the sorted list
    """
    def print_sorted(self):
        new = self[:]
        new.sort()
        print(new)
