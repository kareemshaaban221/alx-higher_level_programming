#!/usr/bin/python3
""" My class module
"""
import unittest
from models.square import Square
from unittest import mock


class TestSquare(unittest.TestCase):
    """ My class
    """

    def setUp(self):
        """_summary_
        """
        Square.setCounter(0)

    def tearDown(self):
        """_summary_
        """
        pass

    def test_instantiation(self):
        """_summary_
        """
        seq1 = Square(2)
        seq2 = Square(4)
        seq3 = Square(6, 0, 0, 500)
        self.assertEqual(seq1.id, 1)
        self.assertEqual(seq1.__dict__, {
            'id': 1,
            '_Rectangle__width': 2,
            '_Rectangle__height': 2,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(seq1)),
            "<class 'models.square.Square'>")
        self.assertEqual(seq2.id, 2)
        self.assertEqual(seq2.__dict__, {
            'id': 2,
            '_Rectangle__width': 4,
            '_Rectangle__height': 4,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(seq2)),
            "<class 'models.square.Square'>")
        self.assertEqual(seq3.id, 500)
        self.assertEqual(seq3.__dict__, {
            'id': 500,
            '_Rectangle__width': 6,
            '_Rectangle__height': 6,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(seq3)),
            "<class 'models.square.Square'>")

    def test_width_property(self):
        """_summary_
        """
        seq1 = Square(2)
        with self.assertRaises(AttributeError):
            print(seq1.__width)
        with self.assertRaises(TypeError):
            seq1.width = '2'
        with self.assertRaises(ValueError):
            seq1.width = 0
        with self.assertRaises(ValueError):
            seq1.width = -5

    def test_height_property(self):
        """_summary_
        """
        seq1 = Square(2)
        with self.assertRaises(AttributeError):
            print(seq1.__height)
        with self.assertRaises(TypeError):
            seq1.height = '2'
        with self.assertRaises(ValueError):
            seq1.height = 0
        with self.assertRaises(ValueError):
            seq1.height = -5

    def test_x_property(self):
        """_summary_
        """
        seq1 = Square(2)
        seq2 = Square(2, 500)
        self.assertEqual(seq2.x, 500)
        with self.assertRaises(AttributeError):
            print(seq1.__x)
        with self.assertRaises(TypeError):
            seq1.x = '2'
        seq1.x = 0
        self.assertEqual(seq1.x, 0)
        with self.assertRaises(ValueError):
            seq1.x = -5

    def test_y_property(self):
        """_summary_
        """
        seq1 = Square(2)
        seq2 = Square(2, 0, 500)
        self.assertEqual(seq2.y, 500)
        with self.assertRaises(AttributeError):
            print(seq1.__y)
        with self.assertRaises(TypeError):
            seq1.y = '2'
        seq1.y = 0
        self.assertEqual(seq1.y, 0)
        with self.assertRaises(ValueError):
            seq1.y = -5

    def test_area(self):
        """_summary_
        """
        seq1 = Square(2)
        self.assertEqual(seq1.area(), 4)
        with self.assertRaises(ValueError):
            seq1 = Square(-1, 3)
        with self.assertRaises(TypeError):
            seq1 = Square('-1', 3)

    def test_display(self):
        """_summary_
        """
        seq1 = Square(2)
        with mock.patch('sys.stdout') as fake_stdout:
            seq1.display()
        fake_stdout.assert_has_calls([
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
        ])

    def test_str(self):
        """_summary_
        """
        seq1 = Square(2)
        self.assertEqual(str(seq1), "[Square] (1) 0/0 - 2")
        seq1.x, seq1.y, seq1.size = 5, 6, 10
        self.assertEqual(str(seq1), "[Square] (1) 5/6 - 10")

    def test_display_x_and_y(self):
        """_summary_
        """
        seq1 = Square(2, 1, 2)
        with mock.patch('sys.stdout') as fake_stdout:
            seq1.display()
        fake_stdout.assert_has_calls([
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write(' '),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
            mock.call.write(' '),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
        ])

    # def test_update_args(self):
    #     """_summary_
    #     """
    #     r1 = Square(10, 10, 10, 10)
    #     self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
    #     r1.update(89)
    #     self.assertEqual(str(r1), "[Square] (89) 10/10 - 10")
    #     r1.update(89, 2)
    #     self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
    #     r1.update(89, 2, 3)
    #     self.assertEqual(str(r1), "[Square] (89) 10/10 - 2")
    #     r1.update(89, 2, 3, 4)
    #     self.assertEqual(str(r1), "[Square] (89) 4/10 - 2")
    #     r1.update(89, 2, 3, 4, 5)
    #     self.assertEqual(str(r1), "[Square] (89) 4/5 - 2")

    # def test_update_kwargs(self):
    #     """_summary_
    #     """
    #     r1 = Square(10, 10, 10, 10)
    #     self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
    #     r1.update(height=1)
    #     self.assertEqual(str(r1), "[Square] (1) 10/10 - 10")
    #     r1.update(width=1, x=2)
    #     self.assertEqual(str(r1), "[Square] (1) 2/10 - 1")
    #     r1.update(y=1, width=2, x=3, id=89)
    #     self.assertEqual(str(r1), "[Square] (89) 3/1 - 2")
    #     r1.update(x=1, height=2, y=3, width=4)
    #     self.assertEqual(str(r1), "[Square] (89) 1/3 - 4")


if __name__ == "__main__":
    unittest.main()
