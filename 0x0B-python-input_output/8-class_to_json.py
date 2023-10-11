#!/usr/bin/python3
"""A module that contains the function 'class_to_json'."""


def class_to_json(obj):
    """A function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj (object): The object to be serialized.

    Returns:
        dict: The dictionary description of 'obj'.
    """
    return {key: value for key, value in obj.__dict__.items()
            if type(value) in [list, dict, str, int, bool]}
