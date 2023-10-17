import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_init(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_id(self):
        s = Square(5, id=99)
        self.assertEqual(s.id, 99)

    def test_size_type_error(self):
        with self.assertRaises(TypeError):
            s = Square("5")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            s = Square(5, x="0")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            s = Square(5, y="0")

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.size * s.size, 25)

    def test_update_args(self):
        s = Square(1, 1, 1, 1)
        s.update(2, 2, 2, 2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

    def test_update_kwargs(self):
        s = Square(1, 1, 1, 1)
        s.update(id=2, size=2, x=2, y=2)
        self.assertEqual(s.id, 2)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 2)

    def test_to_dictionary(self):
        s = Square(5, x=1, y=1, id=1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 5, 'x': 1, 'y': 1})

if __name__ == '__main__':
    unittest.main()
