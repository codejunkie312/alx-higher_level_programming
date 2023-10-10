#!/usr/bin/python3
"""A module that contains the definition of Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """The definition of a Square class"""

    def __init__(self, size):
        """Instantiation function

        Args:
            size (int): a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Calculates the area of a square.

        Returns:
            int : Area of a square
        """
        return self.__size ** 2

    def __repr__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
