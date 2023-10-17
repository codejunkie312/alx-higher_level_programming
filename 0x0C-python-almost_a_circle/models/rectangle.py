#!/usr/bin/python3
"""A module that includes the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """A class representing a rectangle.

    Attributes:
        id (int): The ID of the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int): The x-coordinate of the rectangle.
                y (int): The y-coordinate of the rectangle.
                id (int): The id of the rectangle.
        """
        super().__init__(id)
        attributes = [("width", width), ("height", height), ("x", x), ("y", y)]
        for index, (name, value) in enumerate(attributes):
            if not isinstance(value, int):
                raise TypeError(f"{name} must be an integer")
            if index in [0, 1] and value <= 0:
                raise ValueError(f"{name} must be > 0")
            if index in [2, 3] and value < 0:
                raise ValueError(f"{name} must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Returns the width of a Rectangle instance."""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width of a Rectangle instance."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Returns the height of a Rectangle instance."""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height of a Rectangle instance."""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Returns the value of the private attribute __x."""
        return self.__x

    @x.setter
    def x(self, x):
        """Sets the value of the private attribute __x."""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Returns the value of the private attribute __y."""
        return self.__y

    @y.setter
    def y(self, y):
        """Sets the value of the private attribute __y."""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character '#'."""

        line = " " * self.__x + "#" * self.__width
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(line)

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle.

        Args:
            *args: The new values for the rectangle's attributes in the order:
                id, width, height, x, y.
            **kwargs: The new values for the rectangle's attributes in the
                format: <key name>=<key value>.
        """
        attributes = ["id", "width", "height", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle instance."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of the Rectangle instance."""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
