#!/usr/bin/python3
"""A module that contains the class Student"""


class Student:
    """A class that defines a student by first name, last name, age."""
    def __init__(self, first_name, last_name, age):
        """Instantiation of attributes for class instance.

        Args:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.

        Attributes:
            first_name (str): first name of student.
            last_name (str): last name of student.
            age (int): age of student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in vars(self).items()
                    if key in attrs}
