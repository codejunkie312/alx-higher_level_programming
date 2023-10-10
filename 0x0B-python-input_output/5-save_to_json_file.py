#!/usr/bin/python3
"""This module contains the function 'save_to_json_file'."""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes the JSON representation of an object to a file.

    Args:
        my_obj (object): The object to be serialized.
        filename (str): The name of the file to write to.

    Returns:
        None
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
