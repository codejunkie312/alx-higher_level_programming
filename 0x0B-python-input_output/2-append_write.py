#!/usr/bin/python3
"""A module that includes the function append_write."""


def append_write(filename="", text=""):
    """A function that appends 'text' to the end of the file
    specified.

    Args:
        filename (str): Name of the file.
        text (str): Text to append to the file.

    Returns:
        int: The number of chars appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
