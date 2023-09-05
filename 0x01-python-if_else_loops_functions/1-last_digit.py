#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
isNegative = 0
if (number < 0):
    isNegative = 1
    number *= -1
last_digit = number % 10
if ((last_digit) > 5):
    if (isNegative):
        print(f"Last digit of {-number} is {-last_digit} \
and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif (last_digit < 6 and last_digit != 0):
    if (isNegative):
        print(f"Last digit of {-number} is {-last_digit}\
and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {last_digit} \
and is less than 6 and not 0")
else:
    if (isNegative):
        print(f"Last digit of {-number} is {last_digit} and is 0")
    else:
        print(f"Last digit of {number} is {last_digit} and is 0")
