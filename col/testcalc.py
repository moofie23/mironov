# Запуск тестов: python test_calculator.py -v

# .assertEqual(a, b)	    a == b
# .assertTrue(x)	        bool(x) is True
# .assertFalse(x)	        bool(x) is False
# .assertIs(a, b)	        a is b
# .assertIsNone(x)	        x is None
# .assertIn(a, b)	        a in b
# .assertIsInstance(a, b)	isinstance(a, b)

import unittest
from calc import Calc

class TestCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calc(6, 3)

    def test_sum(self):
        self.assertEqual(self.calc.sum(), 9)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(), 18)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(), 3)

    def test_divide(self):
        self.assertEqual(self.calc.divide(), 2)

if __name__ == '__main__':
    unittest.main()
