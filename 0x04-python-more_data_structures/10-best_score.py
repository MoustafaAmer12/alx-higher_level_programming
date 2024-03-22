#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    val_max = 0
    for k, v in a_dictionary.items():
        if v > val_max:
            val_max = v
            key = k
    if val_max != 0:
        return key
    return
