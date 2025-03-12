import unittest
from daily_problems.maximumCount_2529_12032025 import Solution

class TestMaximumCount(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_all_positive(self):
        self.assertEqual(self.solution.maximumCount([1, 2, 3, 4, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(self.solution.maximumCount([-1, -2, -3, -4, -5]), 5)

    def test_mixed_numbers(self):
        self.assertEqual(self.solution.maximumCount([-1, -2, 0, 1, 2]), 2)

    def test_no_positive_or_negative(self):
        self.assertEqual(self.solution.maximumCount([0, 0, 0]), 0)

    def test_more_positives(self):
        self.assertEqual(self.solution.maximumCount([-1, 1, 2, 3]), 3)

    def test_more_negatives(self):
        self.assertEqual(self.solution.maximumCount([-1, -2, -3, 1]), 3)

if __name__ == '__main__':
    unittest.main()