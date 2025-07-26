import unittest

from katas.find_missing_number import find_missing_number  

class TestFindMissingNumber(unittest.TestCase):

    def test_missing_middle(self):
        self.assertEqual(find_missing_number([3, 0, 1]), 2)
        self.assertEqual(find_missing_number([0, 1, 3, 4, 5]), 2)

    def test_missing_end(self):
        self.assertEqual(find_missing_number([0, 1, 2, 3]), 4)

    def test_missing_start(self):
        self.assertEqual(find_missing_number([1, 2, 3, 4, 5]), 0)

    def test_large_input(self):
        self.assertEqual(find_missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]), 8)

    def test_empty_list(self):
        self.assertEqual(find_missing_number([]), 0)

    def test_single_element(self):
        self.assertEqual(find_missing_number([1]), 0)
        self.assertEqual(find_missing_number([0]), 1)

if __name__ == '__main__':
    unittest.main()
