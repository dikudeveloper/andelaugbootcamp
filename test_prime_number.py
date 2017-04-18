import unittest
from prime_number import generate_prime_numbers


class TestGeneratePrimeNumbers(unittest.TestCase):
    """Tests for prime_number.py"""

    # def setUp(self):
    #     t1 = self.pnum = generate_prime_numbers(5)
    #
    # def test_prime_number_returns_error_message_arg_non_integer(self):
    #     self.assertRaises(ValueError, self.pnum, 1.5)
    #
    # def test_prime_number_returns_error_message_if_arg_negative(self):
    #     """should fail for negative prime numbers"""
    #     self.assertRaises(ValueError, self.pnum, -1)
    #
    # def test_prime_number_returns_error_message_if_arg_zero(self):
    #     """should fail for 0 input"""
    #     self.assertRaises(ValueError, self.pnum, 0)
    #
    # def test_prime_number_returns_error_message_if_arg_one(self):
    #     """should fail for 1 input"""
    #     self.assertRaises(ValueError, self.pnum, 1)
    #
    # def test_prime_number_returns_error_message_if_arg_string(self):
    #     """should fail for string input"""
    #     self.assertRaises(ValueError, self.pnum, 'abc')

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