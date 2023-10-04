#!/usr/bin/python3
"""A module that includes a function that prints a text with 2 new lines after
each of these characters: ., ? and :."""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ? and :.

    Args:
        text (str): The text to print.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char == "\n":
            print(line, end="")
            line = ""
        if char in ".:?" :
            print(line.strip())
            print()
            line = ""
    
    remaining_line = line.strip()
    if remaining_line:
        print(remaining_line)
