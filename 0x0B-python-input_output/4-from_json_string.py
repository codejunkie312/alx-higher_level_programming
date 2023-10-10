#!/usr/bin/python3
"""A module that contains the function 'from_json_string'."""
import json


def from_json_string(my_str):
    """A function that returns an object (python) from JSON string.

    Args:
        my_str (str): String to input.

    Returns:
        object: an object.
    """
    return json.loads(my_str)
