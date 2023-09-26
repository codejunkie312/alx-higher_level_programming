#!/usr/bin/python3
"""
This module contains the class Square
"""


class Square:
    """
    This is the Square class defining a square:
    * Private instance attribute: _size ==> size of square
    * Public instance method: area(self) ==> calculates area of the
        square using the size attribute
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
