import unittest
from prime_number import generate_prime_numbers


class TestGeneratePrimeNumbers(unittest.TestCase):
    """Tests for prime_number.py"""

    def setUp(self):
        self.pnum = generate_prime_numbers

    def test_prime_number_non_integer(self):
        self.assertRaises(ValueError, self.pnum, 1.5)

    def test_prime_number_negative(self):
        """should fail for negative prime numbers"""
        self.assertRaises(ValueError, self.pnum, -1)

    def test_prime_number_not_zero(self):
        """should fail for 0 input"""
        self.assertRaises(ValueError, self.pnum, 0)

if __name__ == '__main__':
    unittest.main()