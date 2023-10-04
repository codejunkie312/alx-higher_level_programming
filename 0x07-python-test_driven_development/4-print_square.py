#!/usr/bin/python3
"""A module that includes a function that prints a square."""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size (int): The size of the square.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
