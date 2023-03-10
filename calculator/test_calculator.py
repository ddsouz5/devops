"""
Unit test for calculator library
"""

import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 0 == calculator.subtract(2, 2)

    def test_multiplication(self):
        assert 4 == calculator.multiply(2, 2)

    def test_division(self):
        assert 1 == calculator.divide(2, 2)
