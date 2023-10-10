#!/usr/bin/python3
"""A module that contains the function read_file (UTF-8) and prints
it to output
"""


def read_file(filename=""):
    """A function that reads a file (UTF-8) and prints it's content
    to the output.

    Args:
        filename (str): file name to read
    """
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
