#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    new_list = my_list[:]
    new_list.reverse()
    if len(new_list):
        for element in new_list:
            print("{:d}".format(element))
    else:
        print()
