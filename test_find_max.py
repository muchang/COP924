# test_find_max.py
import unittest
from find_max import find_max

class TestFindMax(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(find_max([3, 7, 2]), 7)

    def test_with_zero(self):
        self.assertEqual(find_max([0, 10, 5]), 10)

    def test_all_negative_numbers(self):
        # This will FAIL with the current buggy code
        self.assertEqual(find_max([-5, -2, -8]), -2)

    def test_mixed_numbers(self):
        self.assertEqual(find_max([-10, 0, 5, -3]), 5)

if __name__ == '__main__':
    unittest.main()
