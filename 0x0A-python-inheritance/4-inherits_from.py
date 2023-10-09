#!/usr/bin/python3
"""A module that includes a function that checks if a subclass
inheritted directly or indirectly from a specified class"""


def inherits_from(obj, a_class):
    """ Function that checks if a subclass inheritted
    directly or indirectly from a specified class.

    Args:
        obj: Object to check.
        a_class: class to check against.

    Returns:
        bool: True if yes and False if otherwise
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
