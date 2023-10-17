import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_init(self):
        r = Rectangle(1, 2)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)

    def test_id(self):
        r = Rectangle(3, 2, id=89)
        self.assertEqual(r.id, 89)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, x="0")

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, y="0")

    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_update_args(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_update_kwargs(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(id=2, width=2, height=2, x=2, y=2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

    def test_to_dictionary(self):
        r = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1})

if __name__ == '__main__':
    unittest.main()
