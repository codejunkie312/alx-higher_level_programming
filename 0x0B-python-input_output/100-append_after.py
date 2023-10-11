#!/usr/bin/python3
"""A module that contains the function 'append_after'."""


def append_after(filename="", search_string="", new_string=""):
    """A function that inserts a line of text to a file, after each
    line containing a specific string.

    Args:
        filename (str): Name of the file to write.
        search_string (str): Text to search for in the file.
        new_string (str): Text to insert after each line containing
        'search_string'.
    """
    new_content = ""
    with open(filename, "r") as file:
        for line in file:
            new_content += line
            if search_string in line:
                new_content += new_string

    with open(filename, "w") as file:
        file.write(new_content)
