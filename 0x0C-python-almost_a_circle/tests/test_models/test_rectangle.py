import unittest
from unittest.mock import patch
from io import StringIO
import sys
from models.rectangle import Rectangle


class TestRectangle_init(unittest.TestCase):
    """Unit tests for testing instantiation of the Rectangle class."""

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def test_two_args(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(2, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_three_args(self):
        r1 = Rectangle(1, 2, 3)
        r2 = Rectangle(2, 1, 3)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
        r1 = Rectangle(1, 2, 3, 4)
        r2 = Rectangle(2, 1, 3, 4)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(2, 1, 3, 4, 5)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)
        self.assertEqual(r1.id, 5)
        self.assertNotEqual(r1.id, r2.id - 1)


class TestRectangle_width(unittest.TestCase):
    """Unit tests for testing width setter and getter of Rectangle class."""

    def test_width_getter(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)

    def test_width_setter(self):
        r = Rectangle(1, 2)
        r.width = 3
        self.assertEqual(r.width, 3)

    def test_width_setter_type_error(self):
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.width = "3"

    def test_width_setter_value_error(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.width = -3
            r.width = 0


class TestRectangle_height(unittest.TestCase):
    """Unit tests for testing height setter and getter of Rectangle class."""

    def test_height_getter(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.height, 2)

    def test_height_setter(self):
        r = Rectangle(1, 2)
        r.height = 3
        self.assertEqual(r.height, 3)

    def test_height_setter_type_error(self):
        r = Rectangle(1, 2)
        with self.assertRaises(TypeError):
            r.height = "3"

    def test_height_setter_value_error(self):
        r = Rectangle(1, 2)
        with self.assertRaises(ValueError):
            r.height = -3
            r.height = 0


class TestRectangle_x(unittest.TestCase):
    """Unit test for testing x setter and getter of Rectangle class."""

    def test_x_getter(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.x, 3)

    def test_x_setter(self):
        r = Rectangle(1, 2, 3, 4)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_x_setter_type_error(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.x = "5"

    def test_x_setter_value_error(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r.x = -5


class TestRectangle_y(unittest.TestCase):
    """Unit test for testing y setter and getter of Rectangle class."""

    def test_y_getter(self):
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r.y, 4)

    def test_y_setter(self):
        r = Rectangle(1, 2, 3, 4)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_y_setter_type_error(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            r.y = "5"

    def test_y_setter_value_error(self):
        r = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r.y = -5


class TestRectangle_area(unittest.TestCase):
    """Unit tests for testing area method of Rectangle class."""

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)


class TestRectangle_display(unittest.TestCase):
    """Unit tests for testing display method of Rectangle class."""

    def test_display(self):
        r = Rectangle(2, 3)
        expected_output = "##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_with_x(self):
        r = Rectangle(2, 3, 2)
        expected_output = "  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_with_y(self):
        r = Rectangle(2, 3, 0, 2)
        expected_output = "\n\n##\n##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)

    def test_display_with_x_and_y(self):
        r = Rectangle(2, 3, 2, 2)
        expected_output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            r.display()
            self.assertEqual(fake_stdout.getvalue(), expected_output)


class TestRectangle_str(unittest.TestCase):
    """Unit tests for testing __str__ method of Rectangle class."""

    def test_str(self):
        r = Rectangle(1, 2, 3, 4, 5)
        expected_output = "[Rectangle] (5) 3/4 - 1/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            print(r)
            self.assertEqual(fake_stdout.getvalue(), expected_output)


class TestRectangle_update_args(unittest.TestCase):
    """Unit tests for testing update method of Rectangle class with *args."""

    def test_update_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(2, 2, 2, 2, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, r2.id)

    def test_update_args_no_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, r2.id - 1)

    def test_update_args_one_arg(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 2)

    def test_update_args_two_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(2, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, r2.id)

    def test_update_args_three_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(2, 2, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, r2.id)

    def test_update_args_four_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(2, 2, 2, 2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.id, 2)

    def test_update_named_args(self):
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        r1.update(id=2, width=2, height=2, x=2, y=2)
        self.assertEqual(r1.id, 2)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 2)
        self.assertEqual(r1.id, r2.id)


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of Rectangle class."""

    def test_to_dictionary(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r.to_dictionary(),
                         {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1})
