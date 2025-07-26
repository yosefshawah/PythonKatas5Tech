import unittest

from katas.two_sum import two_sum 

class TestTwoSum(unittest.TestCase):

    def test_valid_pair(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_no_pair(self):
        self.assertEqual(two_sum([1, 2, 3, 4, 5], 10), [])

    def test_multiple_pairs(self):
        result = two_sum([1, 2, 3, 4, 3], 6)
        self.assertIn(result, [[1, 3], [2, 4]])  # Either pair is valid

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-1, -2, -3, -4, -5], -8), [2, 4])

    def test_target_zero(self):
        self.assertEqual(two_sum([-3, 4, 3, 90], 0), [0, 2])

    def test_empty_list(self):
        self.assertEqual(two_sum([], 5), [])

    def test_single_element(self):
        self.assertEqual(two_sum([5], 5), [])

if __name__ == '__main__':
    unittest.main()
