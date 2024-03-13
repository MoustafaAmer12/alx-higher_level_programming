#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{:c}".format(
                          ord(str[i]) - 32
                          if ord('a') <= ord(str[i]) <= ord('z')
                          else ord(str[i])),
              end="")
    print("")
