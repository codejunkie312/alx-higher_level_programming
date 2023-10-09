#!/usr/bin/python3
"""Module to check if an object is exactly an instance of a class"""


def is_same_class(obj, a_class):
    """Function to check if an object is exactly an instance of a class.

    Args:
        obj: object to check.
        a_class: class to check against.

    Returns:
        bool: True if the object is exactly an instance of the class,
        False otherwise.
    """
    return type(obj) == a_class
