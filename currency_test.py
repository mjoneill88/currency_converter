import unittest
from currency_converter import *

class TestClass(unittest.TestCase):

    four_dollars = Currency(4, 'USD')
    five_dollars = Currency(5, 'USD')

    def test___init__(self):
        c=Currency(5,'USD')
        self.assertEqual(c.amount, 5)
        self.assertEqual(c.currency_code, 'USD')

    def test__eq__(self):
        self.assertFalse(self.four_dollars == self.five_dollars)

    def test__add__(self):
        self.assertEqual(self.four_dollars + self.five_dollars, Currency(9, 'USD'))

    def test___sub__(self):
        self.assertEqual(self.five_dollars - self.four_dollars, Currency(1, 'USD'))

if __name__=='__main__':
    unittest.main()
