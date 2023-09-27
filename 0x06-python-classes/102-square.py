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
    * getter and a setter for size
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2

    def __lt__(self, square2):
        return self.size < square2.size

    def __le__(self, square2):
        return self.size <= square2.size

    def __eq__(self, square2):
        return self.size == square2.size

    def __ne__(self, square2):
        return self.size != square2.size

    def __gt__(self, square2):
        return self.size > square2.size

    def __ge__(self, square2):
        return self.size >= square2.size
