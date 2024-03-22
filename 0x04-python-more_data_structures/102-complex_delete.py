#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return
    new_dict = {}
    for k, v in a_dictionary.items():
        if v != value:
            new_dict[k] = v
    return new_dict
