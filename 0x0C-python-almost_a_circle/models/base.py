#!/usr/bin/python3
"""
Module that defines a base class for the
project initialization
"""


class Base:
    """Base Class

    Description:
        This class will be the “base” of all other classes in this project.
        The goal of it is to manage id attribute in all your future classes and
        to avoid duplicating the same code by extension, same bugs.

    Attrs:
        private class attribute: __nb_objects
        public instance attribute: id

    Methods:
        __init__: defines calss constructor
    """
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id

    @property
    def id(self):
        return self.id

    @id.setter
    def id(self, id):
        if id:
            self.id = id
        else:
            self.__nb_objects += 1
            self.id = self.__nb_objects
