#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv)
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
