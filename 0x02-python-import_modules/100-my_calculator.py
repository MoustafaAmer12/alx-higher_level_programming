#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    operator = sys.argv[2]
    match(operator):
        case '+':
            print("{} + {} = {}".format(a, b, add(a, b)))
        case '-':
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case '*':
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case '/':
            print("{} / {} = {}".format(a, b, div(a, b)))
        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
