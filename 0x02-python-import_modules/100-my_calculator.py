#!/usr/bin/python3
from sys import argv
from calculator_1 import add, div, mul, sub

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operators = "+-/*"
    operator = argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if operator == "+":
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} {operator} {b} = {mul(a, b)}")
    else:
        print(f"{a} {operator} {b} = {div(a, b)}")
