#!/usr/bin/python3
"""
Module that creates a class with only valid instance attribute
first_name otherwise the instance attribute can't be created
"""
class LockedClass:
    def __getattr__(self, name):
        return self.__dict__[f"{name}"]

    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[f"{name}"] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute 'last_name'")
