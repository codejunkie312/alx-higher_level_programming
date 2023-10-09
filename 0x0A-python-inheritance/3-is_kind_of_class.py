#!/usr/bin/python3
"""Module to check if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Function to check if an object is an instance of a class.

    Args:
        obj: object to check.
        a_class: class to check against.

    Returns:
        bool: True if the object is an instance of the class,
        False otherwise.
    """
    return isinstance(obj, a_class)
