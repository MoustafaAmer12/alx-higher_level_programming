#!/usr/bin/python3
def weight_average(my_list=[]):
    avg, count, weighted = 0, 0, 0
    for i, j in my_list:
        weighted += i*j
        count += j
    if count != 0:
        avg = weighted/count
    return avg
