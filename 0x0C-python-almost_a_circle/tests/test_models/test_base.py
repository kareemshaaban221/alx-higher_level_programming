#!/usr/bin/python3
""" My class module
"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


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

    def test_to_json_string(self):
        """_summary_
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertListEqual(json.loads(json_dictionary), [dictionary])
        json_dictionary = Base.to_json_string([])
        self.assertListEqual(json.loads(json_dictionary), [])
        json_dictionary = Base.to_json_string(None)
        self.assertListEqual(json.loads(json_dictionary), [])
        json_dictionary = Base.to_json_string('wrong type')
        self.assertListEqual(json.loads(json_dictionary), [])

    def test_save_to_file(self):
        """_summary_
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        content = '[]'
        with open("Rectangle.json", "r") as file:
            content = file.read()
        self.assertEqual(
            json.dumps([r1.to_dictionary(),
                        r2.to_dictionary()]),
            content
        )
        s1 = Square(2)
        s2 = Square(4, 2, 8)
        Square.save_to_file([s1, s2])
        content = '[]'
        with open("Square.json", "r") as file:
            content = file.read()
        self.assertEqual(
            json.dumps([s1.to_dictionary(),
                        s2.to_dictionary()]),
            content
        )

    def test_from_json_string(self):
        """_summary_
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertListEqual(
            Base.from_json_string(json_dictionary),
            [dictionary]
        )
        json_dictionary = Base.to_json_string([])
        self.assertListEqual(Base.from_json_string(json_dictionary), [])
        json_dictionary = Base.to_json_string(None)
        self.assertListEqual(Base.from_json_string(json_dictionary), [])
        json_dictionary = Base.to_json_string('wrong type')
        self.assertListEqual(Base.from_json_string(json_dictionary), [])
        self.assertListEqual(Base.from_json_string(None), [])
        self.assertListEqual(Base.from_json_string('[]'), [])

    def test_create(self):
        """_summary_
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        r1 = Rectangle(3, 5)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        r1 = Rectangle(3, 5, 1, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        r1 = Rectangle(3, 5, 1, 1, 55)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        s1 = Square(3)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        s1 = Square(3, 5)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))
        s1 = Square(3, 5, 1, 55)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual(str(s1), str(s2))


if __name__ == "__main__":
    unittest.main()
