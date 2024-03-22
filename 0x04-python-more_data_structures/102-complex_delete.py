#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return
    for k in list(a_dictionary.keys()):
        if a_dictionary[k] == value:
            a_dictionary.pop(k)
    return a_dictionary
