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

class TestBase_save_to_file(unittest.TestCase):
    """Unit tests for testing save_to_file method of Base class."""

    def test_save_to_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_None(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

    def test_save_to_file_empty(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

class TestBase_create(unittest.TestCase):
    """Unit tests for testing create method of Base class."""

    def test_create(self):
        r1 = Rectangle(10, 7, 2, 8)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertIsNot(r1, r2)


class TestBase_load_from_file(unittest.TestCase):
    """Unit tests for testing load_from_file method of Base class."""

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        objs = Rectangle.load_from_file()
        self.assertIsInstance(objs, list)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].__str__(), r1.__str__())
        self.assertEqual(objs[1].__str__(), r2.__str__())

    def test_load_from_file_None(self):
        objs = Rectangle.load_from_file()
        self.assertEqual(objs, [])

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass

class TestBase_save_to_file_csv(unittest.TestCase):
    """Unit tests for testing save_to_file_csv method of Base class."""

    def test_save_to_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_save_to_file_csv_None(self):
        Rectangle.save_to_file_csv(None)
        self.assertFalse(os.path.exists("Rectangle.csv"))

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass


class TestBase_load_from_file_csv(unittest.TestCase):
    """Unit tests for testing load_from_file_csv method of Base class."""

    def test_load_from_file_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        objs = Rectangle.load_from_file_csv()
        self.assertIsInstance(objs, list)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].__str__(), r1.__str__())
        self.assertEqual(objs[1].__str__(), r2.__str__())

    def test_load_from_file_csv_None(self):
        objs = Rectangle.load_from_file_csv()
        self.assertEqual(objs, [])

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass

