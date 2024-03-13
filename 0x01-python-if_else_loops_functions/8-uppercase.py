#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord('a') <= ord(str[i]) <= ord('z'):
            print("{}".format(chr(ord(str[i]) - ord('a') + ord('A')), end= i == len(str) - 1?"\n":"")
        else:
        print("{}".format(str[i], end= i == len(str) - 1?"\n":"")
