#!/usr/bin/python3
"""
This module contains the class Square
"""


class Square:
    """
    This is the Square class defining a square:
    * Private instance attributes:
        ** size ==> size of square
        ** position ==> coordinates of print
    * Public instance methods:
        ** area(self) ==> calculates area of the
            square using the size attribute
        ** my_print(self) ==> that prints in stdout the square
            with the character # in the position mentioned
    * getter and a setter for size
    """
    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif (not isinstance(position, tuple) or len(position) != 2 or
                not all(isinstance(n, int) for n in position) or
                not all(n >= 0 for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        if (not isinstance(position, tuple) or len(position) != 2 or
            not all(isinstance(n, int) for n in position) or
                not all(n >= 0 for n in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print() for y in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for x in range(self.__position[0])]
            [print("#", end="") for j in range(self.__size)]
            print()
