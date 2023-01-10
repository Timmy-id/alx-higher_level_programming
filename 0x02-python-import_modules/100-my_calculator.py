#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def my_calc():
    num_args = len(argv)
    if num_args == 4:
        a = int(argv[1])
        b = int(argv[3])

        if argv[2] == "+":
            print("{:d} + {:d} = {:d}".format(a, b, add(a, b)), end="\n")
        elif argv[2] == "-":
            print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)), end="\n")
        elif argv[2] == "*":
            print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)), end="\n")
        elif argv[2] == "/":
            print("{:d} / {:d} = {:d}".format(a, b, div(a, b)), end="\n")
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>", end="\n")
        exit(1)


if __name__ == "__main__":
    my_calc()
