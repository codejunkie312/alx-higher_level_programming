#!/usr/bin/python3
"""
This module contains the class Square with attributes:
* Private instance attribute: _size
"""


class Square:
    """
    This is the Square class defining a square with attribute size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
