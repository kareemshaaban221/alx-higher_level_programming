#!/usr/bin/python3
""" My class module
"""
import unittest
from models.rectangle import Rectangle
from unittest import mock


class TestRectangle(unittest.TestCase):
    """ My class
    """

    def setUp(self):
        """_summary_
        """
        Rectangle.setCounter(0)

    def tearDown(self):
        """_summary_
        """
        pass

    def test_instantiation(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(4, 5)
        rect3 = Rectangle(6, 7, 0, 0, 500)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.__dict__, {
            'id': 1,
            '_Rectangle__width': 2,
            '_Rectangle__height': 3,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(rect1)),
            "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rect2.__dict__, {
            'id': 2,
            '_Rectangle__width': 4,
            '_Rectangle__height': 5,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(rect2)),
            "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(rect3.id, 500)
        self.assertEqual(rect3.__dict__, {
            'id': 500,
            '_Rectangle__width': 6,
            '_Rectangle__height': 7,
            '_Rectangle__x': 0,
            '_Rectangle__y': 0})
        self.assertEqual(
            str(type(rect3)),
            "<class 'models.rectangle.Rectangle'>")

    def test_width_property(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        with self.assertRaises(AttributeError):
            print(rect1.__width)
        with self.assertRaises(TypeError):
            rect1.width = '2'
        with self.assertRaises(ValueError):
            rect1.width = 0
        with self.assertRaises(ValueError):
            rect1.width = -5

    def test_height_property(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        with self.assertRaises(AttributeError):
            print(rect1.__height)
        with self.assertRaises(TypeError):
            rect1.height = '2'
        with self.assertRaises(ValueError):
            rect1.height = 0
        with self.assertRaises(ValueError):
            rect1.height = -5

    def test_x_property(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(2, 3, 500)
        self.assertEqual(rect2.x, 500)
        with self.assertRaises(AttributeError):
            print(rect1.__x)
        with self.assertRaises(TypeError):
            rect1.x = '2'
        rect1.x = 0
        self.assertEqual(rect1.x, 0)
        with self.assertRaises(ValueError):
            rect1.x = -5

    def test_y_property(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        rect2 = Rectangle(2, 3, 0, 500)
        self.assertEqual(rect2.y, 500)
        with self.assertRaises(AttributeError):
            print(rect1.__y)
        with self.assertRaises(TypeError):
            rect1.y = '2'
        rect1.y = 0
        self.assertEqual(rect1.y, 0)
        with self.assertRaises(ValueError):
            rect1.y = -5

    def test_area(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        self.assertEqual(rect1.area(), 6)
        with self.assertRaises(ValueError):
            rect1 = Rectangle(-1, 3)
        with self.assertRaises(TypeError):
            rect1 = Rectangle('-1', 3)

    def test_display(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        with mock.patch('sys.stdout') as fake_stdout:
            rect1.display()
        fake_stdout.assert_has_calls([
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n'),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n')
        ])

    def test_str(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3)
        self.assertEqual(str(rect1), "[Rectangle] (1) 0/0 - 2/3")
        rect1.x, rect1.y, rect1.width, rect1.height = 5, 6, 10, 11
        self.assertEqual(str(rect1), "[Rectangle] (1) 5/6 - 10/11")

    def test_display_x_and_y(self):
        """_summary_
        """
        rect1 = Rectangle(2, 3, 1, 2)
        with mock.patch('sys.stdout') as fake_stdout:
            rect1.display()
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
            mock.call.write(' '),
            mock.call.write('#'),
            mock.call.write('#'),
            mock.call.write('\n')
        ])

    def test_update_args(self):
        """_summary_
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(str(r1), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """_summary_
        """
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")
        r1.update(width=1, x=2)
        self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r1), "[Rectangle] (89) 3/1 - 2/1")
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

    def test_to_dict(self):
        """_summary_
        """
        r1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r1.to_dictionary(), {
            'x': 3,
            'y': 4,
            'id': 1,
            'height': 2,
            'width': 1
        })
        r1.update(id=58)
        self.assertEqual(r1.to_dictionary(), {
            'x': 3,
            'y': 4,
            'id': 58,
            'height': 2,
            'width': 1
        })


if __name__ == "__main__":
    unittest.main()
