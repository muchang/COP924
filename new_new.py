"""Unit tests for calculate_average_of_evens function."""
import unittest
from tmp import calculate_average_of_evens


class TestCalculateAverageOfEvens(unittest.TestCase):
    """Test cases for the calculate_average_of_evens function."""

    def test_positive_numbers(self):
        """Test with positive numbers."""
        self.assertEqual(calculate_average_of_evens([3, 7, 2]), 7)

    def test_with_zero(self):
        """Test with zero included."""
        self.assertEqual(calculate_average_of_evens([0, 10, 5]), 10)

    def test_all_negative_num(self):
        """Test with all negative numbers."""
        self.assertEqual(calculate_average_of_evens([-5, -2, -8]), -2)

    def test_mixed_numbers(self):
        """Test with mixed positive and negative numbers."""
        self.assertEqual(calculate_average_of_evens([-10, 0, 5, -3]), 5)


if __name__ == '__main__':
    unittest.main()