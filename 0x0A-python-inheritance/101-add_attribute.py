#!/usr/bin/python3
"""Module that contains the function add_attribute."""


def add_attribute(obj, name, value):
    """Function that adds a new attribute to an object if it's possible.

    Args:
        obj: object to add the attribute to.
        name: name of the attribute.
        value: value of the attribute.

    Raises:
        TypeError: if the attribute can't be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
