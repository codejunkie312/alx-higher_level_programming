#!/usr/bin/python3
"""Module that contains the class MyInt that inherits int"""


class MyInt(int):
    """Class that inherits int."""

    def __eq__(self, other):
        """Method to override the == operator."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Method to override the != operator."""
        return int(self) == int(other)
