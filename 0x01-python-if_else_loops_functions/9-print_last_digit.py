#!/usr/bin/python3
def print_last_digit(number):
    num_str = repr(number)
    last_digit = int(num_str[-1])
    print(last_digit, end="")
    return last_digit
