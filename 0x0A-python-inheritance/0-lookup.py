#!/usr/bin/python3
"""Module to lookup attributes and methods of an object"""


def lookup(obj):
    """Function to lookup attributes and methods of an object.

    Args:
        obj: object to lookup.

    Returns:
        list: list of attributes and methods.
    """
    return dir(obj)
