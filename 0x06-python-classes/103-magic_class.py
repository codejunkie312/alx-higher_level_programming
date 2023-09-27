#!/usr/bin/python3
"""
This module contains the class MagicClass
"""


import math


class MagicClass:
    """
    This is the MagicClass class defining a circle:
    * Private instance attribute: radius
    * Instantiation with optional radius
    * Public instance method: area()
    * Public instance method: circumference()
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        else:
            self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
