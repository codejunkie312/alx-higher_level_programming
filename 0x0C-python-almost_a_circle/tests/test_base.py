import unittest
from unittest import mock
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import os

class TestBase(unittest.TestCase):

    def setUp(self):
        Base._Base__nb_objects = 0  # Resetting the __nb_objects to 0 before each test

    def test_init_with_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_init_without_id(self):
        b2 = Base()
        self.assertEqual(b2.id, 1)

    def test_init_invalid_id(self):
        with self.assertRaises(TypeError):
            Base("string")

    def test_to_json_string(self):
        dict_list = [{"id": 1}, {"id": 2}]
        self.assertEqual(Base.to_json_string(dict_list), json.dumps(dict_list))

    def test_from_json_string(self):
        json_str = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(Base.from_json_string(json_str), [{"id": 1}, {"id": 2}])

    def test_save_to_file(self):
        b1 = Square(1)
        b2 = Square(2)
        Square.save_to_file([b1, b2])
        self.assertTrue(os.path.exists("Square.json"))

    def test_load_from_file(self):
        b1 = Square(1)
        b2 = Square(2)
        Square.save_to_file([b1, b2])
        objs = Square.load_from_file()
        self.assertIsInstance(objs, list)
        self.assertIsInstance(objs[0], Base)
        self.assertEqual(objs[0].id, 1)

    @mock.patch('builtins.open', mock.mock_open())
    @mock.patch('csv.writer')
    def test_save_to_file_csv(self, mock_csv_writer):
        b1 = Square(1)
        b2 = Square(2)
        Square.save_to_file_csv([b1, b2])
        mock_csv_writer.assert_called_once()

    @mock.patch('builtins.open', mock.mock_open(read_data='id\n1\n2\n'))
    @mock.patch('csv.reader')
    def test_load_from_file_csv(self, mock_csv_reader):
        mock_csv_reader.return_value = iter([["id"], ["1"], ["2"]])
        objs = Square.load_from_file_csv()
        self.assertIsInstance(objs, list)
        self.assertIsInstance(objs[0], Base)
        self.assertEqual(objs[0].id, 1)


if __name__ == '__main__':
    unittest.main()
