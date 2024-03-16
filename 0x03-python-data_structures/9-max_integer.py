#!/usr/bin/python3
def max_integer(my_list=[]):
    if (not len(my_list)):
        return
    x = my_list[0]
    for element in my_list:
        if x < element:
            x = element
    return x
