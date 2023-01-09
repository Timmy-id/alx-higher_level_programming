#!/usr/bin/python3
from sys import argv


def main():
    num_args = len(argv)
    if num_args == 1:
        print("0 arguments.", end="\n")
    if num_args == 2:
        print("1 argument: ", end="\n")
        print("1: {:s}".format(argv[1]), end="\n")
    if num_args > 2:
        print("{:d} arguments:".format(num_args - 1), end="\n")
        for i in range(1, num_args):
            print("{:d}: {:s}".format(i, argv[i]), end="\n")


if __name__ == "__main__":
    main()
