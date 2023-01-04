#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = (abs(number)) % 10
if number < 0:
    print(f"Last digit of {number} is -{last_digit} and is less than 6 and not 0")
# Last digit of -626 is -6 and is less than 6 and not 0
elif number > 0 and last_digit < 6:
    print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
elif number > 0 and last_digit > 6:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number} is {last_digit} and is 0")
