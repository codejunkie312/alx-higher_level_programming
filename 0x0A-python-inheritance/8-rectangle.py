#!/usr/bin/python3
"""A module that include the definition of the Rectangle
class.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """The definition of Rectangle class."""

    def __init__(self, width, height):
        """Instantiation function

        Args:
            width (int): a positive integer.
            height (int): a positive integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
