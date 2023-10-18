"""Unittest for base.py."""
import unittest
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os


class TestBase_init(unittest.TestCase):
    """Unit tests for testing instantiation of the Base class."""

    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None_id(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_with_arg(self):
        b1 = Base(12)
        b2 = Base(2)
        self.assertEqual(b1.id, 12)
        self.assertEqual(b2.id, 2)

class TestBase_to_json_string(unittest.TestCase):
    """Unit tests for testing to_json_string method of Base class."""

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(type(json_dictionary), str)

    def test_to_json_string_empty(self):
        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, "[]")

    def test_to_json_string_None(self):
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, "[]")

class TestBase_from_json_string(unittest.TestCase):
    """Unit tests for testing from_json_string method of Base class."""

    def test_from_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        dictionary_list = Base.from_json_string(json_dictionary)
        self.assertEqual(type(dictionary_list), list)
        self.assertEqual(dictionary_list[0]['x'], 2)
    
    def test_from_json_string_empty(self):
        dictionary_list = Base.from_json_string("")
        self.assertEqual(dictionary_list, [])

    def test_from_json_string_None(self):
        dictionary_list = Base.from_json_string(None)
        self.assertEqual(dictionary_list, [])
