#!/usr/bin/python3
"""A Module that implements MyInt class
that reverses equality logic for integers
"""


class MyInt(int):
    """A Class that reverses the equality
    logic in integers
    """
    def __eq__(self, other):
        return super().__ne__(other)

    def __ne__(self, other):
        return super().__eq__(other)
