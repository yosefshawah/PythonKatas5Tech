
import unittest
from katas.reduce_list import reduce_array  

class TestReduceArray(unittest.TestCase):

    def test_regular_case(self):
        arr = [10, 15, 7, 20, 25]
        result = reduce_array(arr.copy())
        self.assertEqual(result, [10, 5, -8, 13, 5])

    def test_single_element(self):
        arr = [42]
        result = reduce_array(arr.copy())
        self.assertEqual(result, [42])

    def test_two_elements(self):
        arr = [5, 10]
        result = reduce_array(arr.copy())
        self.assertEqual(result, [5, 5])

    def test_empty_list(self):
        arr = []
        result = reduce_array(arr.copy())
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        arr = [-10, -5, -20]
        result = reduce_array(arr.copy())
        self.assertEqual(result, [-10, 5, -15])

if __name__ == '__main__':
    unittest.main()
