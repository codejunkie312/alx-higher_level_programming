#!/usr/bin/python3
"""This module include the class Rectangle"""


class Rectangle:
    """A rectangle

    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
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

    def area(self):
        """Calculates the area of a rectangle

        Returns:
            (int): The area of a rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of a rectangle

        Returns:
            (int): The perimeter of a rectangle
            0: if `width` or `height` is 0
        """
        if not self.__height or not self.__width:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """String representation of rectangle instances.

        Returns:
            str: A string representing the rectangle as a series of
            '#' characters.

        Notes:
            If ether `height` or `width` is zero, an empty string is returned.
        """
        string = ""
        if not self.__height or not self.__width:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string += "#"
            if i == self.__height - 1:
                continue
            string += "\n"
        return string

    def __repr__(self):
        """Return a string representation of the rectangle suitable for eval.

        Returns:
            str: A string representation of the rectangle in
            the format 'Rectangle(width, height)'.
        """
        return f"Rectangle({self.__width}, {self.height})"
