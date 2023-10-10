#!/usr/bin/python3
"""A module that contains the function 'to_json_string'."""
import json


def to_json_string(my_obj):
    """A function that takes in an object as input and
    returns the JSON representation of it.

    Args:
        my_obj: an object.

    Return:
        str: JSON representation of 'my_obj'.
    """
    return json.dumps(my_obj)
