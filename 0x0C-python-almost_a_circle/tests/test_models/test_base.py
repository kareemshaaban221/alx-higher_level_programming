#!/usr/bin/python3
""" My class module
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ My class
    """

    def setUp(self):
        """_summary_
        """
        Base.setCounter(0)

    def tearDown(self):
        """_summary_
        """
        pass

    def test_instantiation_with_no_args(self):
        """_summary_
        """
        base = Base()
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.id, 1)

    def test_instantiation_with_id(self):
        """_summary_
        """
        base = Base(500)
        self.assertEqual(str(type(base)), "<class 'models.base.Base'>")
        self.assertEqual(base.id, 500)

    def test_access_private_attributes(self):
        """_summary_
        """
        base = Base()
        with self.assertRaises(AttributeError):
            print(base.__nb_objects)

    def test_increment_ids(self):
        """_summary_
        """
        base1, base2, base3 = Base(), Base(), Base()
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)


if __name__ == "__main__":
    unittest.main()
