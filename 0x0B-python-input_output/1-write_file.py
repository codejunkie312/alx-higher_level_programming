#!/usr/bin/python3
"""A module that contains the function write_file."""


def write_file(filename="", text=""):
    """A function that write a text to a file (utf-8).

    Args;
        filename (str): Name of the file to write.
        text (str): Text to write to the file.

    Returns:
        int: The number of chars written to the file.
    """
    with open(filename, "w+", encoding="utf-8") as file:
        return file.write(text)
