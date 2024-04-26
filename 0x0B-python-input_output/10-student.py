#!/usr/bin/python3
"""
A Module that defines a student class
with a student's name and age
"""


class Student:
    """A Student class
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        list_str = True
        if type(attrs) is not list:
            list_str = False
        else:
            for i in attrs:
                if type(i) is not str:
                    list_str = False
        if not list_str:
            return self.__dict__
        new_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
