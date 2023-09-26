#!/usr/bin/python3
"""
This module contains the class Square
"""


class Square:
    """
    This is the Square class defining a square:
    * Private instance attributes: _size ==> size of square
    * Public instance methods:
        ** area(self) ==> calculates area of the
            square using the size attribute
        ** my_print(self) ==> that prints in stdout the square
            with the character #
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

    def my_print(self):
        if not self.__size:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
