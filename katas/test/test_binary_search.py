import unittest
from katas.binary_search import binary_search 

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        self.array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    def test_found(self):
        # Test elements that are in the array
        self.assertEqual(binary_search(self.array, 7), 3)
        self.assertEqual(binary_search(self.array, 1), 0)
        self.assertEqual(binary_search(self.array, 19), 9)
    
    def test_not_found(self):
        # Test elements not in the array
        self.assertEqual(binary_search(self.array, 8), -1)
        self.assertEqual(binary_search(self.array, 0), -1)
        self.assertEqual(binary_search(self.array, 20), -1)

    def test_empty_array(self):
        # Test empty array
        self.assertEqual(binary_search([], 5), -1)

    def test_single_element_array(self):
        # Test array with one element
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 3), -1)

if __name__ == "__main__":
    unittest.main()
