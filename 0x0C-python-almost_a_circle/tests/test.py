import os
import unittest
import doctest
import pycodestyle


class TestDocstrings(unittest.TestCase):
    def setUp(self):
        os.chdir(".")

    def test_docstrings(self):
        for filename in os.listdir("."):
            if filename.endswith(".py"):
                with self.subTest(filename=filename):
                    module = __import__(filename[:-3])
                    self.assertTrue(doctest.testmod(module))


class TestCodeStyle(unittest.TestCase):
    def test_pep8_compliance(self):
        style = pycodestyle.StyleGuide()
        for filename in os.listdir("."):
            if filename.endswith(".py"):
                with self.subTest(filename=filename):
                    result = style.check_files([filename])
                    self.assertEqual(result.total_errors, 0)


if __name__ == "__main__":
    unittest.main()
    