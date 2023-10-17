#!/usr/bin/python3
"""A module that includes the square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class representing a square.

    Attributes:
        id (int): The ID of the square.
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

            Args:
                size (int): The size of the square.
                x (int): The x-coordinate of the square.
                y (int): The y-coordinate of the square.
                id (int): The id of the square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Returns the size of a Square instance."""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of a Square instance."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes of a Square instance."""
        attributes = ["id", "size", "x", "y"]
        if args:
            for i, value in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns a dictionary representation of a Square instance."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returns a string representation of a Square instance."""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.width)
