import unittest
from prime_number import generate_prime_numbers


class TestGeneratePrimeNumbers(unittest.TestCase):
    """Tests for prime_number.py"""

    def test_output_is_list(self):
        """output should be a List"""
        self.assertEqual(True, isinstance(generate_prime_numbers(10), list), msg='Should return a list')

    def test_is_prime_number(self):
        """output should be a prime number"""
        self.assertEqual([2,3,5,7], generate_prime_numbers(10), msg='Should return prime numbers')

    def test_returns_None_if_arg_is_negative(self):
        """There are no prime numbers for negative inputs"""
        self.assertEqual(None, generate_prime_numbers(-10), msg='Should return None for negative argument')

    def test_returns_None_if_arg_is_zero(self):
        """There are no prime numbers for arg 0"""
        self.assertEqual(None, generate_prime_numbers(0), msg='No prime numbers for argument 0')

    def test_returns_None_if_arg_is_one(self):
        self.assertEqual(None, generate_prime_numbers(1), msg='No prime numbers for argument 1')


if __name__ == '__main__':
    unittest.main()