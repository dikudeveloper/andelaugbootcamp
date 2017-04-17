import unittest
from prime_number import generate_prime_numbers


class TestGeneratePrimeNumbers(unittest.TestCase):
    """Tests for prime_number.py"""

    def setUp(self):
        self.pnum = generate_prime_numbers

    def test_prime_number_returns_error_message_arg_non_integer(self):
        self.assertRaises(ValueError, self.pnum, 1.5)

    def test_prime_number_returns_error_message_if_arg_negative(self):
        """should fail for negative prime numbers"""
        self.assertRaises(ValueError, self.pnum, -1)

    def test_prime_number_returns_error_message_if_arg_zero(self):
        """should fail for 0 input"""
        self.assertRaises(ValueError, self.pnum, 0)

    def test_prime_number_returns_error_message_if_arg_one(self):
        """should fail for 1 input"""
        self.assertRaises(ValueError, self.pnum, 1)

    def test_prim_number_returns_error_message_if_arg_string(self):
        """should fail for string input"""
        self.assertRaises(ValueError, self.pnum, 'abc')

if __name__ == '__main__':
    unittest.main()