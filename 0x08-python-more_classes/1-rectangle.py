#!/usr/bin/python3
"""This module include the class Rectangle"""


class Rectangle:
    """A rectangle

    Attributes:
    """
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle.

        Args:
            width: the width of rectangle (default: 0).
            height: The height of rectangle (default: 0).

        Raises:
            TypeError: If `width` is not an integer.
            ValueError: If `width` is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Get the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Set the width of the rectangle.

        Args:
            width (int): The new width value to set.

        Raises:
            TypeError: If `width` or `height` is not an integer.
            ValueError: If `width` or `height` is less than 0.
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Get the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """Set the height of the rectangle.

        Args:
            height (int): The new height value to set.

        Raises:
            TypeError: If `height` is not an integer.
            ValueError: If `height` is less than 0.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
