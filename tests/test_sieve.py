import unittest
from base_algos.sieve import get_primes

class TestSieve(unittest.TestCase):

    def test_get_primes_up_to_10(self):
        self.assertEqual(get_primes(10), [2, 3, 5, 7])

    def test_get_primes_up_to_1(self):
        self.assertEqual(get_primes(1), [])

    def test_get_primes_up_to_0(self):
        self.assertEqual(get_primes(0), [])

    def test_get_primes_up_to_20(self):
        self.assertEqual(get_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

    def test_get_primes_large_input(self):
        self.assertEqual(get_primes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

if __name__ == '__main__':
    unittest.main()