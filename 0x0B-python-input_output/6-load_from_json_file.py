#!/usr/bin/python3
"""A module that contains the 'load_from_json_file' function."""
import json


def load_from_json_file(filename):
    """
    Load JSON data from a file and return a Python object.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        The Python object represented by the JSON data in the file.

    """
    with open(filename, "r") as file:
        return json.loads(file.read())
