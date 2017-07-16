#!/usr/bin/env python3

import stacky
import unittest

class TestIntegers(unittest.TestCase):

    def test_single_integer(self):
        self.assertEqual(stacky.interpret(['5']), [5])

    def test_two_integers(self):
        self.assertEqual(stacky.interpret(['5', '6']), [5, 6])


class TestAdd(unittest.TestCase):

    def test_two_integers(self):
        self.assertEqual(stacky.interpret(['5', '6', '+']), [11])

    def test_two_negative_integers(self):
        self.assertEqual(stacky.interpret(['-5', '-6', '+']), [-11])


class TestSubtract(unittest.TestCase):

    def test_two_integers(self):
        self.assertEqual(stacky.interpret(['6', '5', '-']), [1])

    def test_negative_result(self):
        self.assertEqual(stacky.interpret(['6', '10', '-']), [-4])


class TestMultiply(unittest.TestCase):

    def test_two_integers(self):
        self.assertEqual(stacky.interpret(['5', '6', '*']), [30])

    def test_two_integers_one_negative(self):
        self.assertEqual(stacky.interpret(['-5', '6', '*']), [-30])

    def test_two_negative_integers(self):
        self.assertEqual(stacky.interpret(['-5', '-6', '*']), [30])


if __name__ == '__main__':
    unittest.main()
