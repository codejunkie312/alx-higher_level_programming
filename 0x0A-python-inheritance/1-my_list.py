#!/usr/bin/python3
"""Module that contains the class MyList that inherits list"""


class MyList(list):
    """Class that inherits list."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
