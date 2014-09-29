#! /usr/bin/python

import unittest

from stack import Stack
from calculator import Calculator, Expression, ADD


class TestStack(unittest.TestCase):

    def test_stack(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)

        stack.push('foo')
        stack.push(['bar', 'baz'])

        self.assertEqual(['bar', 'baz'], stack.pop())
        self.assertEqual('foo', stack.pop())
        self.assertEqual(stack.pop(), None)


class TestExpression(unittest.TestCase):

    def test_expression(self):
        operator = None
        literals = None
        with self.assertRaises(ValueError):
            expression = Expression(operator, literals)

        operator = ADD
        with self.assertRaises(TypeError):
            expression = Expression(operator, literals)

        literals = [10000, 1.1]
        expression = Expression(operator, literals)
        self.assertEqual(expression.evaluate(), 10001.1)


class TestCalculator(unittest.TestCase):

    def test_calculator(self):
        bad_stream = ['foo', 'bar', 'baz']
        with self.assertRaises(TypeError):
            Calculator.calculate(bad_stream)

        stream = "1 2 +"
        self.assertEqual(Calculator.calculate(stream), 3)

        stream = "1 2 -"
        self.assertEqual(Calculator.calculate(stream), -1)

        stream = "1 2 *"
        self.assertEqual(Calculator.calculate(stream), 2)

        stream = "1 2 /"
        self.assertEqual(Calculator.calculate(stream), 0.5)

        stream = "3 2 %"
        self.assertEqual(Calculator.calculate(stream), 1)

        complex_stream = (
            " 458.4 -32 +"
            " 90 4 *"
        )
        self.assertEqual(Calculator.calculate(complex_stream), 153504.0)

if __name__ == '__main__':
    unittest.main()
