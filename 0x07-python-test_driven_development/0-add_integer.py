#!/usr/bin/python3
""" A module that includes function add_integer that adds two numbers up """


def add_integer(a, b=98):
    """ Adds two numbers together.
    Args:
        a: an integer or float.
        b: an integer or float (default: 98).
    Returns:
        the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
