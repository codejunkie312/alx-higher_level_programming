import unittest
from models.square import Square

class TestSquar_init(unittest.TestCase):
    """Unit tests for testing instantiation of the Square class."""
    def test_no_arg(self):
        with self.assertRaises(TypeError):
            s = Square()
    
    def test_one_arg(self):
        s1 = Square(2)
        s2 = Square(3)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, s2.id - 1)
    
    def test_two_args(self):
        s1 = Square(2, 3)
        s2 = Square(3, 4)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 3, 4)
        s2 = Square(3, 4, 5)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, s2.id - 1)
    
    def test_four_args(self):
        s1 = Square(2, 3, 4, 5)
        s2 = Square(3, 4, 5, 6)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.id, s2.id - 1)
    
    def test_negative_width(self):
        with self.assertRaises(ValueError):
            s = Square(-1)
    
    def test_zero_width(self):
        with self.assertRaises(ValueError):
            s = Square(0)
    
    def test_negative_x(self):
        with self.assertRaises(ValueError):
            s = Square(1, -1)
    
    def test_negative_y(self):
        with self.assertRaises(ValueError):
            s = Square(1, 1, -1)

class TestSquare_size(unittest.TestCase):
    """Unit tests for testing size setter and getter of Square class."""
    def test_size_getter(self):
        s = Square(1)
        self.assertEqual(s.size, 1)
    
    def test_size_setter(self):
        s = Square(1)
        s.size = 2
        self.assertEqual(s.size, 2)
    
    def test_negative_size(self):
        with self.assertRaises(ValueError):
            s = Square(-1)
    
    def test_zero_size(self):
        with self.assertRaises(ValueError):
            s = Square(0)
    
    def test_size_setter_type_error(self):
        s = Square(1)
        with self.assertRaises(TypeError):
            s.size = "2"

class TestSquare_x(unittest.TestCase):
    """Unit tests for testing x setter and getter of Square class."""
    def test_x_getter(self):
        s = Square(1, 2)
        self.assertEqual(s.x, 2)
    
    def test_x_setter(self):
        s = Square(1, 2)
        s.x = 3
        self.assertEqual(s.x, 3)
    
    def test_negative_x(self):
        with self.assertRaises(ValueError):
            s = Square(1, -1)
    
    def test_x_setter_type_error(self):
        s = Square(1, 2)
        with self.assertRaises(TypeError):
            s.x = "3"

class TestSquare_y(unittest.TestCase):
    """Unit tests for testing y setter and getter of Square class."""
    def test_y_getter(self):
        s = Square(1, 2, 3)
        self.assertEqual(s.y, 3)
    
    def test_y_setter(self):
        s = Square(1, 2, 3)
        s.y = 4
        self.assertEqual(s.y, 4)
    
    def test_negative_y(self):
        with self.assertRaises(ValueError):
            s = Square(1, 2, -3)
    
    def test_y_setter_type_error(self):
        s = Square(1, 2, 3)
        with self.assertRaises(TypeError):
            s.y = "4"

class TestSquare_area(unittest.TestCase):
    """Unit tests for testing area method of Square class."""
    def test_area(self):
        s = Square(2)
        self.assertEqual(s.area(), 4)

class TestSquare_update(unittest.TestCase):
    """Unit tests for testing update method of Square class."""
    def test_update_args_one(self):
        s = Square(1)
        s.update(2)
        self.assertEqual(s.id, 2)
    
    def test_update_args_two(self):
        s = Square(1)
        s.update(2, 3)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
    
    def test_update_args_three(self):
        s = Square(1)
        s.update(2, 3, 4)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
    
    def test_update_args_four(self):
        s = Square(1)
        s.update(2, 3, 4, 5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)
    
    def test_update_named_args_one(self):
        s = Square(1)
        s.update(id=2)
        self.assertEqual(s.id, 2)

    def test_update_named_args_two(self):
        s = Square(1)
        s.update(id=2, size=3)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
    
    def test_update_named_args_three(self):
        s = Square(1)
        s.update(id=2, size=3, x=4)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
    
    def test_update_named_args_four(self):
        s = Square(1)
        s.update(id=2, size=3, x=4, y=5)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 5)


class TestSquare_to_dictionary(unittest.TestCase):
    """Unit tests for testing to_dictionary method of Square class."""
    def test_to_dictionary(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(s.to_dictionary(), {'id': 4, 'size': 1, 'x': 2, 'y': 3})
    
class TestSquare_str(unittest.TestCase):
    """unit tests for testing __str__ method of Square class."""
    def test_str(self):
        s = Square(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] ({}) 2/3 - 1".format(s.id))
    
    def test_str_no_id(self):
        s = Square(1, 2, 3)
        self.assertEqual(str(s), "[Square] ({}) 2/3 - 1".format(s.id))
    
    def test_str_no_x(self):
        s = Square(1, 0, 3, 4)
        self.assertEqual(str(s), "[Square] ({}) 0/3 - 1".format(s.id))
    
    def test_str_no_y(self):
        s = Square(1, 2, 0, 4)
        self.assertEqual(str(s), "[Square] ({}) 2/0 - 1".format(s.id))
    
    def test_str_no_args(self):
        with self.assertRaises(TypeError):
            s = Square()
    
    def test_str_extra_args(self):
        with self.assertRaises(TypeError):
            s = Square(1, 2, 3, 4, 5)
                