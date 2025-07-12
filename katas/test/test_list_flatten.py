import unittest
from katas.list_flatten import flatten_list  

class TestFlattenList(unittest.TestCase):
    def test_regular_nested_list(self):
        nested = [1, [2, 3], [4, [5, 6]], 7]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4, 5, 6, 7])

    def test_empty_list(self):
        nested = []
        self.assertEqual(flatten_list(nested), [])

    def test_flat_list(self):
        nested = [1, 2, 3, 4]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4])

    def test_deeply_nested(self):
        nested = [[[[[1]]]], 2, [3, [4, [5]]]]
        self.assertEqual(flatten_list(nested), [1, 2, 3, 4, 5])

    def test_single_element_nested(self):
        nested = [[[[[5]]]]]
        self.assertEqual(flatten_list(nested), [5])

    def test_mixed_types(self):
        nested = [1, [2, [3, ["a"]]]]
        result = flatten_list(nested)
        self.assertIn("a", result)  # not type-safe, just confirms function handles other types
        self.assertEqual(result, [1, 2, 3, "a"])  # function appends any non-list type

if __name__ == '__main__':
    unittest.main()
